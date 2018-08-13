import praw
import csv
import inspect
import copy

# class MRARedditScraper:
#     def __init__(self, reddit = praw.Reddit()):
#         self.output_filename = ""
#         self.output_directory = ""
#         self.reddit = reddit

def main(subreddit_name, submission_id):
    client_id = 'PCmdhrO8vLNGjw'
    client_secret = 'Q6f3xbnnNK4UdkuIstpWbbC2q_4'
    password = 'whateverwhocares'
    user_agent = 'testscript by /u/memescholar'
    memescholar = 'memescholar'

    reddit = praw.Reddit(client_id=client_id,
                         client_secret=client_secret,
                         password=password,
                         user_agent=user_agent,
                         username=memescholar)
    subreddit = reddit.subreddit(subreddit_name)
    submission = reddit.submission(id=submission_id)
    row_header = [subreddit_name, submission_id, submission.title]
    row = copy.copy(row_header)
    row.append("submission")
    row.append(submission.selftext.encode('UTF-8'))
    rows = [row]
    for comment in submission.comments.list():
        # only save off actual comment bodies (ignore MoreComment, etc objects)
        if isinstance(comment,praw.models.reddit.comment.Comment):
            row = copy.copy(row_header)
            row.append("comment")
            row.append(comment.body.encode('UTF-8'))
            rows.append(row)

    with open('blah.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file, dialect='excel-tab', quoting=csv.QUOTE_ALL)
        csv_writer.writerows(rows)

main(subreddit_name='TheRedPill', submission_id='6sbx6i')
