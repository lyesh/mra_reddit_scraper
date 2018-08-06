CREATE TABLE posters
(
    id BigInt PRIMARY KEY,
    reddit_id VarChar(500)

);

CREATE TABLE subreddits
(
    id BigInt PRIMARY KEY,
    name VarChar(500)
);

CREATE TABLE submissions
(
    id BigInt PRIMARY KEY,
    reddit_id VarChar(100),
    subreddit_id BigInt,
    text VarChar(41000),
    CONSTRAINT submissions_fk1 FOREIGN KEY (subreddit_id) REFERENCES subreddits (id)
);

CREATE TABLE comments
(
    id BigInt PRIMARY KEY ,
    reddit_id VarChar(100),
    submission_id BigInt,
    text LongVarChar(41000),
    CONSTRAINT comments_fk1 FOREIGN KEY (submission_id) REFERENCES submissions (id)
);
