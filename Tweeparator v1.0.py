import sys
import tweepy
from tweepy import api

__author__ = '@ManasKocharekar'


#KEYS
CUST_KEY = '7TfeHq5DOg5zidfSTbP15mL4L'
CUST_SECRET = 'wkn03374J04tbgqoE8UemjfjfXJBKy4fQM8G8jFpuNd4nhrDKc'
APP_KEY = '936617132963463168-0kTv9jK0kAxougV5rQlHIMJOos1zTLK'
APP_SECRET = 'GaspSZqoO6sA9Q7W9YBYQIZDRSTFcOItcaZ8sdBWLk19r'
auth = tweepy.OAuthHandler(CUST_KEY, CUST_SECRET)
auth.set_access_token(APP_KEY, APP_SECRET)

access = tweepy.API(auth)

TweetThis = str(sys.argv[1])

if TweetThis.startswith("#"):
    TweetText = TweetThis[1:]
else:
    filename = open(TweetThis, 'r')
    TweetText = filename.read()
    filename.close()

print(TweetText)

if len(TweetText) <= 280:
    access.update_status(TweetText)
    print('Tweeted Successfully')
else:
    print('Tweet Length Exceeded')
