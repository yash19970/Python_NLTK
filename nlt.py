import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, PunktSentenceTokenizer
from nltk.corpus import stopwords, state_union
from nltk.stem import PorterStemmer

text = "hello there, how are you doing today? The this weather is awesome."
print(sent_tokenize(text))
print '\n'
# stopwords
words = word_tokenize(text)
stop_words = set(stopwords.words("english"))
#print (stop_words)
filtered_sentance = []

for w in words:
	if w not in stop_words:
		filtered_sentance.append(w)

#print filtered_sentance

#STEMING

ps = PorterStemmer()
ex_list = ["python","pythoner","pythoning","pythoned","pythonly"]
# for w in ex_list:
# 	print ps.stem(w)
print '\n'
text = "It is very important to be pythonly when youre pythonning with python"
words = word_tokenize(text)
for w in words:
	print ps.stem(w)


# SPEECH TAGGING. PunktSentenceTokenizer - unsupervised ML tokenizer

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_token = PunktSentenceTokenizer(train_text)
tokenized = custom_sent_token.tokenize(sample_text)

def process_content():
	for i in tokenized:
		words = nltk.word_tokenize(i)
		tagged = nltk.pos_tag(words)

		#print(tagged)
process_content()


# CHUNKING


