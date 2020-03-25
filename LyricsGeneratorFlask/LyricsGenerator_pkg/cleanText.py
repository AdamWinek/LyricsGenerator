import string

def load_doc(doc):
    #open file and convert to text
    file = open(doc, 'r')
    text = file.read()
    return text

def clean_doc(text):
    # replace '--' with a space ' '
    text = text.replace("-", " ")
    # delete apostophes
    text = text.replace("'", "")
    #make text lower case
    text = text.lower()
    #Replacing lyrical tags
    text = text.replace("[chorus]", "")
    text = text.replace("[chorus 2]", "")
    text = text.replace("[chorus 3]", "")
    text = text.replace("[chorus 4]", "")
    text = text.replace("[verse]", "")
    text = text.replace("[verse 2]", "")
    text = text.replace("[verse 3]", "")
    text = text.replace("[verse 4]", "")
    text = text.replace("[brige]", "")
    text = text.replace("[brige 2]", "")
    text = text.replace("[brige 3]", "")
    text = text.replace("[brige 4]", "")
    text = text.replace("(","")
    text = text.replace(")","")
    text = text.replace("[","")
    text = text.replace("]","")

    #seperate by whitespace
    words = text.split()
    #remove punctuation 
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in words]
    return stripped

input_file =  'LyricsGeneratorFlask/static/LyricsGenerator_pkg/g=drakeLyrics.txt'

text = load_doc(input_file)
tokens = clean_doc(text)


# organize into sequences of tokens
length = 8 + 1
sequences = list()
for i in range(length, len(tokens)):
	# select sequence of tokens
	seq = tokens[i-length:i]
	# convert into a line
	line = ' '.join(seq)
	# store
	sequences.append(line)
print('Total Sequences: %d' % len(sequences))

# save sequences to file
out_filename = 'LyricsGeneratorFlask/static/LyricsGenerator_pkg/lyrics_sequences.txt'
data = '\n'.join(sequences)
file = open(out_filename, 'w')
file.write(data)
file.close()