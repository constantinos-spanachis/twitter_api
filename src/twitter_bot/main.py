import tweepy

from src.utils.helper_functions import create_twitter_api, limit_handle


class GenerousBot:
	def __init__(self):
		self.api = create_twitter_api()
	
	def follow_followers(self):
		# Generous BOT
		try:
			for follower in limit_handle(tweepy.Cursor(self.api.followers).items(), time_sleep=20):
				if follower.follwers_count > 10:
					follower.follow()
					print(f"Followed {follower.name}")
		except RuntimeError:
			print("You have no followers...")
		except Exception as e:
			print(f"Something went wrong. Error was {e}")
			raise e


class NarcissistBot:
	def __init__(self):
		self.api = create_twitter_api()
	
	def favorite_tweet(self, search_string: str, number_of_tweets: int):
		for tweet in limit_handle(tweepy.Cursor(self.api.search, search_string).items(number_of_tweets)):
			try:
				tweet.favorite()
				print("I liked that tweet")
			except tweepy.TweepError as e:
				print(e.reason)
			except RuntimeError:
				break


NarcissistBot().favorite_tweet("python", 2)


