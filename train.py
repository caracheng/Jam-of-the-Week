import csv

def readStatus(path, posPath, negPath):
    pos = []
    neg = []
    count = 0
    with open(path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            comment = row["comment_message"]
            print comment
            sentiment = raw_input("Classify the comment as p or n: ")
            if sentiment == "p":
                    pos.append(comment)
            if sentiment == "n":
                    neg.append(comment)
            count += 1
            if count == 500:
                break
    with open(posPath, 'wb') as nameFile:
        wr = csv.writer(nameFile, quoting=csv.QUOTE_ALL)
        wr.writerow(pos)
    with open(negPath, 'wb') as nameFile:
        wr = csv.writer(nameFile, quoting=csv.QUOTE_ALL)
        wr.writerow(neg)

def countComments(path):
    """Counts the total number of names in a list """
    numOfComments = 0
    with open(path, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            numOfComments = len(row)
    print numOfComments

countComments('pos_comments.csv')
#readStatus('facebook_comments.csv', 'pos_comments.csv', 'neg_comments.csv')