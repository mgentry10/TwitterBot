import tweepy
import time
from credentials import *
from weather import *

hashtags = ['#weather', '#LIWeather', '#NYWeather', '#LongIsland', 'Commack', '#Suffolk']


def hashtag_append():
    hashtags.append(hashtag1)
    hashtags.append(hashtag2)


def hashtag_pop():
    hashtags.pop(0)
    hashtags.pop(0)


def sleep():
    time.sleep(3600)


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

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
    hashtag_append()
    hashtag_pop()
    sleep()
    continue
