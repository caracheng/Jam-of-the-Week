import csv

def readStatus(path, posPath, sugPath, unPath):
    positive = []
    suggestive = []
    unrelated = []
    count = 0
    with open(path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            comment = row["comment_message"]
            print comment
            sentiment = raw_input("Classify the comment as p, s or u: ")
            if sentiment == "p":
                    positive.append(comment)
            if sentiment == "s":
                    suggestive.append(comment)
            if sentiment == "u":
                    unrelated.append(comment)
            count += 1
            if count == 500:
                break
    with open(posPath, 'wb') as nameFile:
        wr = csv.writer(nameFile, quoting=csv.QUOTE_ALL)
        wr.writerow(positive)
    with open(sugPath, 'wb') as nameFile:
        wr = csv.writer(nameFile, quoting=csv.QUOTE_ALL)
        wr.writerow(suggestive)
    with open(unPath, 'wb') as nameFile:
        wr = csv.writer(nameFile, quoting=csv.QUOTE_ALL)
        wr.writerow(unrelated)

def countComments(path):
    """Counts the total number of names in a list """
    numOfComments = 0
    with open(path, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            numOfComments = len(row)
    print numOfComments

#countComments('pos_comments.csv')
readStatus('facebook_comments.csv', 'pos_comments.csv', 'sug_comments.csv', 'unrelated_comments.csv')