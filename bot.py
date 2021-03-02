# import all library
import tweepy
import time


# Twitter key configration
CONSUMER_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXX"
CONSUMER_SECRET = "XXXXXXXXXXXXXXXXXXXXXX"
ACCESS_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXX"
ACCESS_SECRET = "XXXXXXXXXXXXXXXXXXXXXXXX"


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# change the Hash tag here
hashtag = ("Example")

# Number of the retweets
tweet_number = 100
tweets = tweepy.Cursor(api.search, hashtag).items(tweet_number)


def main():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("Retweet Completed!")
            time.sleep(10)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(10)


if __name__ == "__main__":
    main()
