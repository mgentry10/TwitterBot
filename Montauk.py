import tweepy
import time
import datetime
from credentials import *
from weather import *
import random

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
hashtags = ['#weather', '#LIWeather', '#NYWeather', '#LongIsland', 'Montauk', '#EastLI', '#EasternLI']

weather = Weather(unit=Unit.FAHRENHEIT)
location = weather.lookup_by_location('11572')
conditionTemp = location.condition.temp
condition = location.condition

while True:
    tweet = 'It is ' + str(condition.text).lower() + ' and ' + str(conditionTemp) + chr(176) +  \
            ' in Montauk, NY.' + random.choice(hashtags) + ' ' + random.choice(hashtags) + ' ' + random.choice(hashtags)
    api.update_status(status=tweet)
    time.sleep(3600)
    continue
