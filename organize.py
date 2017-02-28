import csv

def readStatus(path, malePath, femalePath):
    """Opens CSV file, reads it in and creates a data structure where every row is a dictionary.
    Writes to two CSV file lists of male and female names"""
    maleAuthor = []
    femaleAuthor = []
    with open(path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row["status_author"]
            if name not in femaleAuthor and name not in maleAuthor:
                print name
                inferredGender = raw_input("Infer the gender of this name. Type m or f: ")
                if inferredGender == "m":
                        maleAuthor.append(name)
                if inferredGender == "f":
                        femaleAuthor.append(name)
    with open(malePath, 'wb') as nameFile:
        wr = csv.writer(nameFile, quoting=csv.QUOTE_ALL)
        wr.writerow(maleAuthor)
    with open(femalePath, 'wb') as nameFile:
        wr = csv.writer(nameFile, quoting=csv.QUOTE_ALL)
        wr.writerow(femaleAuthor)

def countNames(path):
    numOfAuthors = 0
    with open(path, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            numOfAuthors = len(row)
    print numOfAuthors

#readStatus('facebook_statuses.csv', 'maleAuthors.csv', 'femaleAuthors.csv')
#countNames('femaleAuthors.csv') # 38 unique names
#countNames('maleAuthors.csv')   #317 unique names

# TO DO
"""Write a function that collects all the posts by the females/males and
counts the number of total reactions and number of specific reactions.
Average them out by number of posts - total number of (specific) reactions / total number of male/female statuses"""

