# text classifier for sentimental analysis.
import nltk,pickle
import random
from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier


documents = [(list(movie_reviews.words(fileid)),category)
			for category in movie_reviews.categories()
			for fileid in movie_reviews.fileids(category)]

# for category in movie_reviews():
# for fileid in movie_reviews.fileids(category):
# documents.append(list(movie_reviews.words(fileid)),category)
random.shuffle(documents)
#print documents[1]

all_words = []
for w in movie_reviews.words():
	w = w.lower()
	all_words.append(w)
print '\n'

# convert to nltk freq distribution
all_words = nltk.FreqDist(all_words)
#print all_words.most_common(15)
# number of times stupic appears.
#print all_words["stupid"]
# TRAINING DATASET.
word_features = list(all_words.keys())[:3000]
def find_features(document):
	words = set(document)
	features = {}
	for w in word_features:
		features[w] = (w in words)
	return features
#print find_features(movie_reviews.words('neg/cv000_29416.txt'))
feature_sets = [(find_features(rev), category) for (rev,category) in documents]

#NAIVE BAIS ALGO.
training_set = feature_sets[:1900]
testing_set = feature_sets[1900:]
#classifier  = nltk.NaiveBayesClassifier.train(training_set)

classifier_file = open("naivebayes.pickle","rb")
classifier  = pickle.load(classifier_file)
classifier_file.close()

print nltk.classify.accuracy(classifier,training_set)*100
classifier.show_most_informative_features(15)
#using pickle to save python objects. (save classifier)

# save_classifier = open("naivebayes.pickle","wb")
# pickle.dump(classifier, save_classifier) #save into classifier.
# save_classifier.close()
 
