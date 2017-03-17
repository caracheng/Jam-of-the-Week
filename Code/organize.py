import csv
from decimal import Decimal

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
    """Counts the total number of names in a list """
    numOfAuthors = 0
    with open(path, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            numOfAuthors = len(row)
    return numOfAuthors

#readStatus('facebook_statuses.csv', 'maleAuthors.csv', 'femaleAuthors.csv')
#countNames('femaleAuthors.csv') # 38 unique names          355 total unique authors
#countNames('maleAuthors.csv')   #317 unique names


# TO DO
"""Write a function that collects all the posts by the females/males and
counts the number of total reactions and number of specific reactions.
Average them out by number of posts - total number of (specific) reactions / total number of male/female statuses"""

def reactionDistribution(path, list):
    """Creates a distribution of all the reactions, comments, shares, likes, etc...on the posts made by male/female authors."""
    distribution = {}
    nameList = []
    totalReactions = 0
    totalComments = 0
    totalShares = 0
    totalLikes = 0
    totalLoves = 0
    totalWows = 0
    totalHahas = 0
    totalSads = 0
    totalAngrys = 0
    with open(list, 'rb') as authorFile:
        femAuthors = csv.reader(authorFile)
        for name in femAuthors:
            for author in name:
                nameList.append(author)
    with open(path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["status_author"] in nameList:
                reactions = row["num_reactions"]
                comments = row["num_comments"]
                shares = row["num_shares"]
                likes = row["num_likes"]
                loves = row["num_loves"]
                wows = row["num_wows"]
                hahas = row["num_hahas"]
                sads = row["num_sads"]
                angrys = row["num_angrys"]
                totalReactions += int(reactions)
                totalComments += int(comments)
                totalShares += int(shares)
                totalLikes += int(likes)
                totalLoves += int(loves)
                totalWows += int(wows)
                totalHahas += int(hahas)
                totalSads += int(sads)
                totalAngrys += int(angrys)
    distribution['totalReactions'] = totalReactions
    distribution['totalComments'] = totalComments
    distribution['totalShares'] = totalShares
    distribution['totalLikes'] = totalLikes
    distribution['totalLoves'] = totalLoves
    distribution['totalWows'] = totalWows
    distribution['totalHahas'] = totalHahas
    distribution['totalSads'] = totalSads
    distribution['totalAngrys'] = totalAngrys
    return distribution

#reactionDistribution('facebook_statuses.csv','femaleAuthors.csv')
#{'totalSads': 1, 'totalLikes': 2129, 'totalComments': 197, 'totalHahas': 7, 'totalReactions': 2365, 'totalWows': 13, 'totalShares': 54, 'totalLoves': 215, 'totalAngrys': 0}
#reactionDistribution('facebook_statuses.csv','maleAuthors.csv')
#{'totalSads': 11, 'totalLikes': 25555, 'totalComments': 2646, 'totalHahas': 196, 'totalReactions': 27505, 'totalWows': 360, 'totalShares': 3845, 'totalLoves': 1371, 'totalAngrys': 12}

def details(path, list):
    """Calculates the total number of comments/shares per author. Calculated the percentages of each form of FB reactions"""
    distribution = reactionDistribution(path, list)
    numAuthors = float(countNames(list))
    totalReactions = float(distribution['totalReactions'])
    print "Avg # of comments per author: ", round(distribution['totalComments']/numAuthors, 2)
    print "Avg # of shares per author: ", round(distribution['totalShares'] / numAuthors, 2)
    print "Total % of likes", distribution['totalLikes']/totalReactions
    print "Total % of loves", distribution['totalLoves']/totalReactions
    print "Total % of wows", distribution['totalWows']/totalReactions
    print "Total % of hahas", distribution['totalHahas']/totalReactions
    print "Total % of sads", distribution['totalSads']/totalReactions
    print "Total % of angry", distribution['totalAngrys']/totalReactions

#details('facebook_statuses.csv','femaleAuthors.csv')
"""
Avg # of comments per author:  5.18
Avg # of shares per author:  1.42
Total % of likes 0.90021141649
Total % of loves 0.0909090909091
Total % of wows 0.00549682875264
Total % of hahas 0.00295983086681
Total % of sads 0.000422832980973
Total % of angry 0.0
"""

#details('facebook_statuses.csv','maleAuthors.csv')
"""
Avg # of comments per author:  8.35
Avg # of shares per author:  12.13
Total % of likes 0.929103799309
Total % of loves 0.0498454826395
Total % of wows 0.0130885293583
Total % of hahas 0.00712597709507
Total % of sads 0.000399927285948
Total % of angry 0.000436284311943
"""
