import string

def load_doc(doc):
    #open file and convert to text
    file = open(doc, 'r')

    text = file.read()
    return text

def clean_doc(text):


    #get rid of repeated lines
    lines = text.splitlines()
     
    repeat_count = 0
    for i in range(len(lines)- 1):
        if lines[i] == lines[i + 1]:
            repeat_count += 1
    print(repeat_count)
    
    for i in range(len(lines) - repeat_count):
        if lines[i] == lines[i + 1]:
            lines.pop(i + 1)
        lines[i] = lines[i] + " newline"

    text = "\n".join(lines[1:])
    


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

input_file =  'LyricsGeneratorFlask/home/g=drakeLyrics.txt'

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
out_filename = 'LyricsGeneratorFlask/home/lyrics_sequences.txt'
data = '\n'.join(sequences)
file = open(out_filename, 'w')
file.write(data)
file.close()