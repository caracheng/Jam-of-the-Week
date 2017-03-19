import nltk
import csv
import preClassify

#Based off of http://www.laurentluce.com/posts/twitter-sentiment-analysis-using-python-and-nltk/

def collectComments(path, sentiment):
    allComments = []
    with open(path, 'rb') as commentFile:
        commentsFem = csv.reader(commentFile)
        for row in commentsFem:
            for comment in row:
                tup = (comment, sentiment)
                allComments.append(tup)
    return allComments

pos_comments = collectComments('pos_comments.csv', "positive")

sug_comments = collectComments('sug_comments.csv', "suggestive")

unrelated_comments = collectComments('unrelated_comments.csv', "unrelated")

def makeComments():
    comments = []
    for (words, sentiment) in pos_comments:
        words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
        comments.append((words_filtered, sentiment))
    for (words, sentiment) in sug_comments:
        words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
        comments.append((words_filtered, sentiment))
    for (words, sentiment) in unrelated_comments:
        words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
        comments.append((words_filtered, sentiment))
    return comments

def get_words_in_comments(comments):
    all_words = []
    for (words, sentiment) in comments:
      all_words.extend(words)
    return all_words

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features

word_features = get_word_features(get_words_in_comments(makeComments()))

def extract_features(document): #document/input is a single tweet/comment
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

training_set = nltk.classify.apply_features(extract_features, makeComments())

classifier = nltk.NaiveBayesClassifier.train(training_set)

tweet = 'suggestion'
print classifier.classify(extract_features(tweet.split()))
