import tweepy
import time
from credentials import *
from weather import *
import random

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
hashtags = ['#weather', '#LIWeather', '#NYWeather', '#LongIsland', '#Oceanside', '#Nassau']

weather = Weather(unit=Unit.FAHRENHEIT)
location = weather.lookup_by_location('11572')
conditionTemp = location.condition.temp
condition = location.condition

while True:
    hashtag1 = random.choice(hashtags)
    hashtag2 = random.choice(hashtags)
    hashtag3 = random.choice(hashtags)

    tweet = 'It is ' + str(condition.text).lower() + ' and ' + str(conditionTemp) + chr(176) +  \
            ' in Oceanside, NY. ' + hashtag1 + ' ' + hashtag2 + ' ' + hashtag3
    api.update_status(status=tweet)
    time.sleep(3600)
    continue
