import tweepy
import time
from credentials import *
from weather import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

weather = Weather(unit=Unit.FAHRENHEIT)
location = weather.lookup_by_location('11572')
conditionTemp = location.condition.temp
condition = location.condition

while True:
    tweet = 'It is currently ' + conditionTemp + chr(176) + ' and ' + str(condition.text).lower() + ' in Montauk, NY. ' \
        '#weather #LIWeather #NYWeather #LongIsland'
    api.update_status(status=tweet)
    time.sleep(3600)
