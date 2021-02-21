# import all library
import tweepy
import configparser
import time
import logging


# Twitter key configration
CONSUMER_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXX"
CONSUMER_SECRET = "XXXXXXXXXXXXXXXXXXXXXX"
ACCESS_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXX"
ACCESS_SECRET = "XXXXXXXXXXXXXXXXXXXXXXXX"


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


hashtag = ( "UnityForEthiopia")

tweet_number = 10
tweets = tweepy.Cursor(api.search, hashtag).items(tweet_number)


def searchbot():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("Retweet Done!")
            time.sleep(10)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(10)


searchbot()
