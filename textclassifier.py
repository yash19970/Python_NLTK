# text classifier for sentimental analysis.
import nltk,pickle
import random
from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB,GaussianNB, BernoulliNB
from sklearn.linear_model import LogisticRegression,SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from nltk.classify import ClassifierI
from scipy.stats import mode

class VoteClassifier(ClassifierI):
	def __init__(self, *classifiers):
		self._classifiers = classifiers

	def classify(self,features):
		votes = []
		for c in self._classifiers:
			v = c.classify(features)
			votes.append(v)
		return mode(votes)
	def confidence(self,features):
		votes = []
		for c in self._classifiers:
			v = c.classify(features)
			votes.append(v)
		choice_votes  = votes.count(mode(votes))
		conf = choice_votes / len(votes) #certainty.
		return conf


documents = [(list(movie_reviews.words(fileid)),category)
			for category in movie_reviews.categories()
			for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)

all_words = []
for w in movie_reviews.words():
	w = w.lower()
	all_words.append(w)
print '\n'
# convert to nltk freq distribution
all_words = nltk.FreqDist(all_words)
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


#MULTINOMIAL NB: EXAMPLES.
MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print 'MNB Classifier: \n'
print nltk.classify.accuracy(MNB_classifier,testing_set)*100

BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
BernoulliNB_classifier.train(training_set)
print 'BernoulliNB Classifier: \n'
print nltk.classify.accuracy(BernoulliNB_classifier,testing_set)*100

LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
LogisticRegression_classifier.train(training_set)
print 'LogisticRegression Classifier: \n'
print nltk.classify.accuracy(LogisticRegression_classifier,testing_set)*100

SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
SGDClassifier_classifier.train(training_set)
print 'SGDClassifier Classifier: \n'
print nltk.classify.accuracy(SGDClassifier_classifier,testing_set)*100

LinearSVC_classifier = SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(training_set)
print 'LinearSVC Classifier: \n'
print nltk.classify.accuracy(LinearSVC_classifier,testing_set)*100

NuSVC_classifier = SklearnClassifier(NuSVC())
NuSVC_classifier.train(training_set)
print 'NuSVC Classifier: \n'
print nltk.classify.accuracy(NuSVC_classifier,testing_set)*100

#NEW CLASSIFIER with voting.

voted_classifier  = VoteClassifier(classifier,SGDClassifier_classifier,MNB_classifier,BernoulliNB_classifier,NuSVC_classifier,LinearSVC_classifier)
print 'Voted Classifier accuracy percent: \n'
print nltk.classify.accuracy(voted_classifier,testing_set)*100

#print 'Classification:',voted_classifier.classify(testing_set[0][0]),'\n confidence:',voted_classifier.confidence(testing_set[0][0])

