from cleanText import load_doc
import numpy as np
from pickle import dump
from keras.preprocessing.text import Tokenizer
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Embedding

in_file = "lyrics_sequences.txt"

text = load_doc(in_file)
#split the sequences up line by line
lines = text.split('\n')
#next we need to substitute each word for an integer token unique to that word
#to do this I will use the tokenizer class keras provides
tokenizer = Tokenizer()
tokenizer.fit_on_texts(lines)
# sequences = tokenizer.texts_to_sequences(lines)
original_sequences = tokenizer.texts_to_sequences(lines)
vocab_size = len(tokenizer.word_index) + 1
max_len = 9
aligned_sequneces = []
for sequence in original_sequences:
    aligned_sequence = np.zeros(max_len, dtype=np.int64)
    aligned_sequence[:len(sequence)] = np.array(sequence, dtype=np.int64)
    aligned_sequneces.append(aligned_sequence)

sequences = np.array(aligned_sequneces)

# vocabulary size
vocab_size = len(tokenizer.word_index) + 1
print('Vocabulary Size: %d' % vocab_size)
#In the model I will be using we are going to use 8 word seequences as input and 1 word as output
#breaking up the sequences into input and output
sequences = np.array(sequences)
print(sequences)
X = sequences[:,:-1]
y = sequences[:,-1]
y = to_categorical(y, num_classes=vocab_size)
print(y)
seq_length = X.shape[1]


# define model
model = Sequential()
model.add(Embedding(vocab_size, 50, input_length=seq_length))
model.add(LSTM(100, return_sequences=True))
model.add(LSTM(100))
model.add(Dense(100, activation='relu'))
model.add(Dense(vocab_size, activation='softmax'))
print(model.summary())
# compile model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit model
model.fit(X, y, batch_size=60, epochs=100)

# save the model to file
model.save('model.h5')
# save the tokenizer
dump(tokenizer, open('tokenizer.pkl', 'wb'))
