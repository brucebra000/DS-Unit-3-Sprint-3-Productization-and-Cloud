import os
from dotenv import load_dotenv
import tweepy

load_dotenv()

TWITTER_API_KEY = os.getenv("TWITTER_API_KEY", default="OOPS")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET", default="OOPS")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN", default="OOPS")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET", default="OOPS")

auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
print(type(auth))
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

client = tweepy.API(auth)
print(type(client))
print(dir(client))
print("----------")

my_tweets = client.home_timeline()

for tweet in my_tweets:
    print(type(tweet), tweet.text)
    print("----------")

other_tweets = client.user_timeline("elonmusk", tweet_mode = 'extended')

for tweet in other_tweets:
    print(type(tweet), tweet.full_text)
