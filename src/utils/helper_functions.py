import os
import tweepy
from dotenv import load_dotenv, find_dotenv


def check_env() -> None:
	"""Checks for a .env file in any of the subdirectories of your current file."""
	if load_dotenv(find_dotenv()):
		print("Successfully loaded the environment variables.")
	else:
		print("No environment was found. Please create a .env file using the .env.example")
		
		
def create_twitter_api() -> tweepy.API:
	"""
	Creates a twitter api using the required credentials and keys found in the .env file.
	
	Returns:
		The twitter api.
	"""
	check_env()
	
	env_variable_keys = {"TWITTER_API_KEY", "TWITTER_SECRET_KEY", "TWITTER_ACCESS_TOKEN", "TWITTER_ACCESS_SECRET"}

	assert env_variable_keys.issubset(os.environ.keys()), "Check if you have the correct creds in your .env file"
	
	auth = tweepy.OAuthHandler(os.getenv("TWITTER_API_KEY"), os.getenv("TWITTER_SECRET_KEY"))
	
	auth.set_access_token(os.getenv("TWITTER_ACCESS_TOKEN"), os.getenv("TWITTER_ACCESS_SECRET"))
	
	api = tweepy.API(auth)
	return api


def limit_handle(cursor: tweepy.Cursor, time_sleep: int = 1000):
	"""
	Handles the Tweepy Cursor in order to avoid timeouts.
	Args:
		cursor: The tweepy cursor.
		time_sleep: The time you want to break if a timeout occurs.

	Returns:
		The cursor's next value.
	"""
	import time
	
	try:
		while True:
			yield cursor.next()
	except tweepy.RateLimitError:
		time.sleep(time_sleep)
	except StopIteration:
		print("No more items to loop through.")
