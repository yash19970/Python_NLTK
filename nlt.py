import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, PunktSentenceTokenizer
from nltk.corpus import stopwords, state_union, wordnet as wn
from nltk.stem import PorterStemmer, WordNetLemmatizer

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
#for w in words:
	#print ps.stem(w)


# SPEECH TAGGING. PunktSentenceTokenizer - unsupervised ML tokenizer

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")
#custom_sent_token = PunktSentenceTokenizer(train_text)
#tokenized = custom_sent_token.tokenize(sample_text)

def process_content():
	for i in tokenized:
		words = nltk.word_tokenize(i)
		tagged = nltk.pos_tag(words)

		#print(tagged)
#process_content()


# Named Entity REcog
# def process_content():
# 	for i in tokenized:
# 		words = nltk.word_tokenize(i)
# 		tagged = nltk.pos_tag(words)
# 		namedEnt  = nltk.ne_chunk(tagged)
# 		namedEnt.draw()
# 		print(tagged)
# process_content()

#Lemmatizing - same as STEMMING, end result is real word.

lemmatizer = WordNetLemmatizer()
print lemmatizer.lemmatize("cats")
print lemmatizer.lemmatize("cacti")
print lemmatizer.lemmatize("rocks")

 
#wordnet - sysnonyms and antonyms.
syns = wn.synsets("good")[0]
print syns.definition()
print syns.lemma_names()
print "\n"
#print syns[0].meaning()
#print syns[0].examples()
synonym = []
antonyms = []
for syn in wn.synsets("good"):
	for l in syns.lemmas():
		synonym.append(l.name())
		if l.antonyms():
			antonyms.append(l.antonyms()[0].name())
print set(synonym)
print set(antonyms)

#SIMILARITY
w1 = wn.synset("ship.n.01")
w2 = wn.synset("boat.n.01")
print w1.wup_similarity(w2)






