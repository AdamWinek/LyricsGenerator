from random import randint
from pickle import load
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
import string

import json

def load_doc(doc):
    #open file and convert to text
    file = open(doc, 'r')
    text = file.read()
    return text

def generate_seq(model, tokenizer, seq_length, seed_text, n_words):
	result = list()
	in_text = seed_text
	# generate a fixed number of words
	for _ in range(n_words):
		# encode the text as integer
		encoded = tokenizer.texts_to_sequences([in_text])[0]
		# truncate sequences to a fixed length
		encoded = pad_sequences([encoded], maxlen=seq_length, truncating='pre')
		# predict probabilities for each word
		yhat = model.predict_classes(encoded, verbose=0)
		# map predicted word index to word
		out_word = ''
		for word, index in tokenizer.word_index.items():
			if index == yhat:
				out_word = word
				break
		# append to input
		in_text += ' ' + out_word
		result.append(out_word)
	return ' '.join(result)


def getJsonFile( userLyrics):
	in_file = "home/lyrics_sequences.txt"
	doc = load_doc(in_file)
	lines = doc.split('\n')

	seq_length = len(lines[0].split()) - 1

	#load model 
	model = load_model('home/model.h5')
	# load the tokenizer
	tokenizer = load(open('home/tokenizer.pkl', 'rb'))


	#take user input and make sure it is valid
	#remove words if it is too long
	#seed text
	seed_text = userLyrics
	#changes the string so it will work with the model
	seed_text = seed_text.lower()

	#remove punctuation
	seed_text = seed_text.translate(str.maketrans('', '', string.punctuation))

	#seed_text = lines[randint(0,len(lines))]
	print(seed_text + '\n')

	# generate new text
	generated = seed_text + '\n' + generate_seq(model, tokenizer, seq_length, seed_text, 100)

	
	print(generated)
	# data = {
    # "returnInfo": generated
	# }
	return generated
	# with open("/users/adamwinek/LyricsGenerator/lyrics.json", "w") as write_file:
	# 	(json.dump(data, write_file))
	# return write_file
getJsonFile("dont like my math teacher he sucks ass")


 