from bot.fizzbuzzjazz import FizzBuzzJazz
from bot.twitter import make_tweet


def lambda_handler(event, context):
    fbj_value = FizzBuzzJazz().get_fizzbuzzjazz(event)
    make_tweet(fbj_value)
