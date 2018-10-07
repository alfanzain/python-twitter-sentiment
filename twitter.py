import tweepy
from textblob import TextBlob

#import pandas as pd
#import numpy as np

from credentials import *

def twitter_setup():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)
    return api

extractor = twitter_setup()

public_tweets = extractor.search('#game')

for tweet in public_tweets:
    print(tweet.text)
    # analysis = TextBlob(tweet.text)
    # print(analysis.sentiment)