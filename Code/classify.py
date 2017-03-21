import nltk
import csv
import preClassify

#Based off of http://www.laurentluce.com/posts/twitter-sentiment-analysis-using-python-and-nltk/

def collectComments(path, sentiment):
    "Collects comments from CSV and creates a list composed of a tuple (comment, sentiment) to be used in a training set"
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
    """Takes the training set and creates a single tuple list. Cleans the training set of any word smaller than 2 characters"""
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
    """Creates a list of distinct words in the comments"""
    all_words = []
    for (words, sentiment) in comments:
      all_words.extend(words)
    return all_words

def get_word_features(wordlist):
    """Orders the list of words from the comments by the frequency in which they appear"""
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features

word_features = get_word_features(get_words_in_comments(makeComments()))

def extract_features(document):
    """Takes a single comment as input and returns a a dictionary indicating what words are contained in the input passed"""
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

training_set = nltk.classify.apply_features(extract_features, makeComments())

classifier = nltk.NaiveBayesClassifier.train(training_set)

def classifyComments(statuses, authors, comments):
    """Takes the set of comments made on male/female posts, classifies them on the classifier trained on the training set,
    and returns a dictionary detailing how many comments were classified as positive, suggestive or unrelated"""
    distribution = {}
    pos = 0
    sug = 0
    unrelated = 0
    commentList = preClassify.grabComments(statuses, authors, comments)
    for comment in commentList:
        classifiedComment = classifier.classify(extract_features(comment.split()))
        if classifiedComment == "positive":
            pos += 1
        if classifiedComment == "suggestive":
            sug += 1
        if classifiedComment == "unrelated":
            unrelated +=1
    distribution["positive"] = pos
    distribution["suggestive"] = sug
    distribution["unrelated"] = unrelated
    return distribution

#classifyComments('facebook_statuses.csv','femaleAuthors.csv', 'facebook_comments.csv' ) #yielded {'positive': 184, 'suggestive': 0, 'unrelated': 32}
#classifyComments('facebook_statuses.csv','maleAuthors.csv', 'facebook_comments.csv' ) #{'positive': 2401, 'suggestive': 10, 'unrelated': 468}

testCase = [("This is great work! Keep it up", 'positive'),
            ("I think you can improve this by doing X", 'suggestive'),
            ("You can prob feed your cat", 'unrelated'),
            ("YOU ROCK BRO", 'positive'),
            ("I have a few suggestions for you", 'suggestive'),
            ("I hope you get into BLLLLOOOOOOO", 'positive'),
            ("Nice", 'positive'),
            ("Thanks", 'unrelated'),
            ("You really need to work on", 'suggestive'),
            ("That's some great jazz", 'positive'),
            ("What can i do to get better", 'suggestive'),
            ("What sound system do you use", "unrelated"),
            ("You could totally rock that so much more if you just tuned your guitar a bit more", 'suggestive'),
            ("BROOOOOO", "positive"),
            ("DUDE", "positive"),
            ("Thanks bro", "unrelated"),
            ("How are you doing", "unrelated"),
            ("Just came from Italy", "unrelated"),
            ("How about trying this instead of that?", "suggestive")
]

def calculateAccuracy(statuses, authors, comments):
    """Attempting to calculate accuracy of the model"""
    comments = []
    for (words, sentiment) in testCase:
        words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
        comments.append((words_filtered, sentiment))
    wFeatures = nltk.classify.apply_features(extract_features, comments)
    accuracy = nltk.classify.accuracy(classifier, wFeatures) #what in the world kinda format do you take in???????
        # avgAccuracy += accuracy
    print accuracy

calculateAccuracy('facebook_statuses.csv','femaleAuthors.csv', 'facebook_comments.csv')
