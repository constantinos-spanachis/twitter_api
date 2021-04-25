import os
import tweepy
from dotenv import load_dotenv, find_dotenv


def check_env():
	if load_dotenv(find_dotenv()):
		print("Successfully loaded the environment variables.")
	else:
		print("No environment was found. Please create a .env file using the .env.example")
		
		
def create_twitter_api():
	check_env()
	
	env_variable_keys = {"TWITTER_API_KEY", "TWITTER_SECRET_KEY", "TWITTER_ACCESS_TOKEN", "TWITTER_ACCESS_SECRET"}

	assert env_variable_keys.issubset(os.environ.keys()), "Check if you have the correct creds in your .env file"
	
	auth = tweepy.OAuthHandler(os.getenv("TWITTER_API_KEY"), os.getenv("TWITTER_SECRET_KEY"))
	
	auth.set_access_token(os.getenv("TWITTER_ACCESS_TOKEN"), os.getenv("TWITTER_ACCESS_SECRET"))
	
	api = tweepy.API(auth)
	return api


def limit_handle(cursor, time_sleep=1000):
	from time import time
	try:
		while True:
			yield cursor.next()
	except tweepy.RateLimitError:
		time.sleep(time_sleep)
	except StopIteration:
		print("No more items to loop through.")
