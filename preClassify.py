import csv

def grabStatusIDs(path, list):
    """Returns a dictionary of the status_id and the author of their posts. """
    nameList=[]
    statusID = {}
    with open(list, 'rb') as authorFile:
        femAuthors = csv.reader(authorFile)
        for name in femAuthors:
            for author in name:
                nameList.append(author)
    with open(path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["status_author"] in nameList:
                statusID[row["status_id"]] = row["status_author"]
    return statusID

def grabComments(path, statusList, commentList):
    """Grabs comments on psots made by female/male authors that are not made by themselves"""
    comments = []
    statusIDs = grabStatusIDs(path, statusList) #dictionary
    with open(commentList) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["status_id"] in statusIDs: #if the comment is made on the post by an female author
                if row["comment_author"] != statusIDs[row["status_id"]]:     #if the comment poster is not the original poster herself
                    comments.append(row["comment_message"])
    return comments


grabComments('facebook_statuses.csv','femaleAuthors.csv', 'facebook_comments.csv')
#grabStatusIDs('facebook_statuses.csv','femaleAuthors.csv')
