import tweepy
import time
from credentials import *
from weather import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

weather = Weather(unit=Unit.FAHRENHEIT)
location = weather.lookup_by_location('11725')
condition = location.condition.temp


while True:
    tweet = 'The current temperature in Commack, NY is: ' + condition + chr(176)

    api.update_status(status=tweet)

    time.sleep(3600)
