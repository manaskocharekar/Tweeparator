import sys
import tweepy
from tweepy import api
from nltk.tokenize import sent_tokenize


__author__ = '@ManasKocharekar'

#KEYS
CUST_KEY = 'CUST_KEY'
CUST_SECRET = 'CUST_SECRET'
APP_KEY = 'APP_TOKEN'
APP_SECRET = 'APP_SECRET'
auth = tweepy.OAuthHandler(CUST_KEY, CUST_SECRET)
auth.set_access_token(APP_KEY, APP_SECRET)

access = tweepy.API(auth)

TweetThis = str(sys.argv[1])

filename = open(TweetThis, 'r')
TweetText = filename.read()
filename.close()

print(TweetText)

if len(TweetText) <= 280:
    access.update_status(TweetText)
    print('Tweeted Successfully')
else:
    print('Tweet Length Exceeded')
