import tweepy
import time
from credentials import *
from weather import *
import random

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
hashtags = ['#weather', '#LIWeather', '#NYWeather', '#LongIsland', 'Commack', '#Suffolk']

weather = Weather(unit=Unit.FAHRENHEIT)
location = weather.lookup_by_location('11572')
conditionTemp = location.condition.temp
condition = location.condition

while True:
    hashtag1 = hashtags[0]
    hashtag2 = hashtags[1]

    tweet = 'It is ' + str(condition.text).lower() + ' and ' + str(conditionTemp) + chr(176) +  \
            ' in Commack, NY. ' + hashtag1 + ' ' + hashtag2 + ' '
    api.update_status(status=tweet)
    hashtags.append(hashtag1)
    hashtags.append(hashtag2)
    hashtags.pop(0)
    hashtags.pop(0)
    time.sleep(3600)
    continue
