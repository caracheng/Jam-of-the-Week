import csv

def readStatus(path, posPath, negPath):
    pos = []
    neg = []
    with open(path) as csvfile:
        reader = csv.DictReader(csvfile)
        while len(pos)+len(neg) != 1000:
            for row in reader:
                comment = row["comment_message"]
                print comment
                sentiment = raw_input("Classify the comment as p or n: ")
                if sentiment == "p":
                        pos.append(comment)
                if sentiment == "n":
                        neg.append(comment)
    with open(posPath, 'wb') as nameFile:
        wr = csv.writer(nameFile, quoting=csv.QUOTE_ALL)
        wr.writerow(pos)
    with open(negPath, 'wb') as nameFile:
        wr = csv.writer(nameFile, quoting=csv.QUOTE_ALL)
        wr.writerow(neg)

