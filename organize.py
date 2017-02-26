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
            print name
            inferredGender = raw_input("Infer the gender of this name. Type m or f: ")
            if inferredGender == "m":
                if name not in maleAuthor:
                    maleAuthor.append(name)
            if inferredGender == "f":
                if name not in femaleAuthor:
                    femaleAuthor.append(name)
    with open(malePath, 'wb') as nameFile:
        wr = csv.writer(nameFile, quoting=csv.QUOTE_ALL)
        wr.writerow(maleAuthor)
    with open(femalePath, 'wb') as nameFile:
        wr = csv.writer(nameFile, quoting=csv.QUOTE_ALL)
        wr.writerow(femaleAuthor)

readStatus('facebook_statuses.csv', 'maleAuthors.csv', 'femaleAuthors.csv')

