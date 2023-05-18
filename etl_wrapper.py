import pandas
import s3fs
import tweepy
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
user_key = os.getenv("USER_KEY")
user_secret = os.getenv("USER_SECRET")


#Authentication
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(user_key, user_secret)


# Configuring an API object
api = tweepy.API(auth)

tweets = api.user_timeline(
    screen_name = '@elonmusk',
    count=200, #Maximum Limit : 200 | Defaut : 20
    include_rts=False, #Extracts re-tweets
)


#Extracting data from Twitter API
print(tweets)