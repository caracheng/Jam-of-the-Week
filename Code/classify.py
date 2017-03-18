import nltk
import csv
import preClassify


def collectComments(path):
    allComments = []
    with open(path, 'rb') as commentFile:
        commentsFem = csv.reader(commentFile)
        for row in commentsFem:
            for comment in row:
                allComments.append(comment)
    print allComments

pos_comments = collectComments('pos_comments.csv')

neg_comments = collectComments('neg_comments.csv')

test_tweets = [(['feel', 'happy', 'this', 'morning'], 'positive'),
    (['larry', 'friend'], 'positive'),
    (['not', 'like', 'that', 'man'], 'negative'),
    (['house', 'not', 'great'], 'negative'),
    (['your', 'song', 'annoying'], 'negative')]

def makeTweets():
    tweets = []
    for (words) in pos_comments + neg_comments:
        words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
        tweets.append((words_filtered))
    return tweets

def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
      all_words.extend(words)
    return all_words

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features

word_features = get_word_features(get_words_in_tweets(makeTweets()))

def extract_features(document): #document/input is a single tweet/comment
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

training_set = nltk.classify.apply_features(extract_features, makeTweets())
classifier = nltk.NaiveBayesClassifier.train(training_set)

tweet = 'Larry is my friend'
print classifier.classify(extract_features(tweet.split()))

