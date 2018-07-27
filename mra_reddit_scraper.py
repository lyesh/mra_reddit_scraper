import praw
import os
import csv
from pprint import pprint

reddit = praw.Reddit(client_id='PCmdhrO8vLNGjw',
                     client_secret='Q6f3xbnnNK4UdkuIstpWbbC2q_4',
                     password='whateverwhocares',
                     user_agent='testscript by /u/memescholar',
                     username='memescholar')

subreddit = reddit.subreddit('TheRedPill')
submission = reddit.submission(id='6sbx6i')
threadId = str(subreddit) + str(submission)

print(subreddit)
print(submission.title)
print(threadId)

print(submission.title)
print(submission.selftext)
submission.comments.replace_more(limit=3)
for top_level_comment in submission.comments:
    print(top_level_comment.body)

submissioninfo = submission.title + submission.selftext
print(submissioninfo)

submission.comments.replace_more(limit=3)
comment_queue = submission.comments[:]  # Seed with top-level
while comment_queue:
    comment = comment_queue.pop(0)
    print(comment.body)
    comment_queue.extend(comment.replies)

threadId = str(subreddit) + str(submission)

content = str(submission.comments.replace_more(limit=3))

def writeToTxtFile(threadId, content):

    pprint(content)
    filename = "output/" + threadId + ".txt"
    file = open(filename,"a")
    file.write(content)
    file.close()


    results = []
with open('inputfile.txt') as inputfile:
    for line in inputfile:
        results.append(line.strip().split(','))

writeToTxtFile(threadId, content)

import csv
csvData = [["Submission", submissioninfo], ["Comments", comment.body], ["Replies", comment.replies]]
csvFilename = "output/" + threadId + ".csv"

def writeToCsvFile(csvFilename, csvData):
    # file = open(csvFilename,"w")
    # wr = csv.writer(csvFilename, dialect='excel')
    # file.wr(csvData)
    # file.close()

    # using the 'with' format here is good practice for a touple of reasons.
    # the issue was you trying to write to the file directly, instead of using the special csv writer you'd prepped
    with open(csvFilename, 'a') as file:
        wr = csv.writer(file, quoting=csv.QUOTE_ALL, dialect='excel')
        wr.writerow(csvData)
        file.close()