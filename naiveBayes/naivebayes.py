import re
from collections import defaultdict

# get distinct words out of the txt file
def tokenize(message):
	message = message.lower()
	all_words = re.findall("[a-z0-9']+", message)
	return set(all_words)

# for training set we will create a datastructure to work with, it
# will count the words in a labeled training set of mesages. We'll have it
# return a dictionary whose kezs are words, and whose values are two-element
# lists, spame_count, non_spam_count

def count_words(training_set):
	""" 
	training set consists of pairs (message, is_spam)
	"""
	counts = defaultdict(lambda: [0,0])
	for message, is_spam in training_set:
		for word in tokenize(message):
			counts[word][0 if is_spam else 1] += 1

	return counts

"""
The next step is to turn these counts into estimated probabilities using the smothing
"""

def word_probabilities(counts, total_spams, total_non_spams, k=0.5):
	"""
	Turn the word counts into a list of triplets w, p(w|spam), p(w|spam~)
	"""

	return [(w,
			 (spam + k)/(total_spams + 2 * k)
			 (non_spam + k)/ (total_non_spams + 2*k))
			 for w, (spam, non_spam) in counts.iteritems()]

"""
Last piece is to use these word probs (and of course the naive bayes assumption)
to assign probabilities to tese messages:
"""

def spam_probability(word_probs, mesage):
	message_words = tokenize(message)
	log_prob_if_spam = log_prob_if_not_spam = 0.0

	# iterate through each word in our vocabulary
	for word, prob_if_spam, prob_if_not_spam in word_probs:
		# if word appears in the message,
		# add the log probability of seeing it
		if word in message_words:
			log_prob_if_spam += math.log(prob_if_spam)
			log_prob_if_not_spam += math.log(prob_if_not_spam)

		# if word doesnt appear in the message add the log probability
		# of not seeing it which is ofcourse (1- probability of seeing it)
		else:
			log_prob_if_spam += math.log(1.0 - prob_if_spam)
			log_prob_if_not_spam += math.log(1.0 - prob_if_not_spam)

		prob_if_spam = math.exp(log_prob_if_spam)
		prob_if_not_spam = math.exp(log_prob_if_not_spam)

# we can put all of this together into a naive bayes classifier
def NaiveBayesClassifer:
	def __init__(self, k=0.5):
		self.k = k
		self.word_probs = []

	def train(self, training_set):
		# count spam and non spam message
		num_spams = len([is_spam
						 for message, is_spam in training_set
						 if is_spam])
		num_non_spams = len(training_set) - num_spams

		# run training data through our pipeline
		word_counts = count_words(training_set)
		self.word_probs = word_probabilities(word_counts, num_spams, num_non_spams, self.k)

		def classify(self, message):
			return spam_probability(self.word_probs, message)

# Lets get this party started and actually do some machine learning with some testing
