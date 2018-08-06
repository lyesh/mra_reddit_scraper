import praw
import sqlite3

subreddit_id_query = "SELECT * FROM subreddits WHERE name=?;"


def main(subreddit_name, submission_id, database):
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

    database.execute()

    subreddit = reddit.subreddit(subreddit_name)
    get_subreddit_id()
    submission = reddit.submission(id=submission_id)
    threadId = subreddit.display_name + submission.id
    print subreddit.fullname
    print submission.title
    print submission.selftext
    for comment in submission.comments.list():
        if comment.body:
            print comment.body

def connectToSql():
    db = sqlite3.connect(":memory:")
    script = open('resources/create_post_db.sql')
    scriptString = ""
    for line in script.readlines():
        scriptString += line
    db.executescript(scriptString)
    return db

sqliteDB = connectToSql()
main(subreddit='TheRedPill', submissionId='6sbx6i', database=sqliteDB)
