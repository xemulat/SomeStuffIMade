import praw

# Set up PRAW with your Reddit app credentials
client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'
username = 'YOUR_REDDIT_USERNAME'
password = 'YOUR_REDDIT_PASSWORD'
user_agent = f'web:com.xem.isafe:v1.0.0 (by u/{username})'

# minimum score
minscore = 6

# Initialize the Reddit API client
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     username=username,
                     password=password,
                     user_agent=user_agent)

# Retrieve all posts from the specified user
user = reddit.redditor(username)

# Iterate through the user's posts and print information about each post
for submission in user.submissions.new():
    if submission.score <= minscore:
        print('Title:', submission.title)
        print('Score:', submission.score)
        print('URL:', submission.url)
        print('------------------------')
