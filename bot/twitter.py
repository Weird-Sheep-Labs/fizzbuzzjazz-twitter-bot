import os

import tweepy


def make_tweet(fbj_value: str):
    client = tweepy.Client(
        consumer_key=os.environ["TWITTER_CONSUMER_KEY"],
        consumer_secret=os.environ.get("TWITTER_CONSUMER_KEY_SECRET"),
        access_token=os.environ.get("TWITTER_ACCESS_TOKEN"),
        access_token_secret=os.environ.get("TWITTER_ACCESS_TOKEN_SECRET"),
    )
    client.create_tweet(text=fbj_value)
