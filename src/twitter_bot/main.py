import tweepy

from src.utils.helper_functions import create_twitter_api, limit_handle


class GenerousBot:
	"""
	A bot that follows back any of your followers that has more that a number of followers.
	"""
	def __init__(self):
		self.api = create_twitter_api()
	
	def follow_followers(self, number_of_followers: int) -> None:
		"""
		Follows your followers if they have more than a number of followers themselves.
		
		Args:
			number_of_followers: The number of followers your follower needs to have in order to follow them back.
		
		Raises:
			Any error that is not a Runtime Error.
		"""
		try:
			for follower in limit_handle(tweepy.Cursor(self.api.followers).items(), time_sleep=20):
				if follower.follwers_count > number_of_followers:
					follower.follow()
					print(f"Followed {follower.name}")
		except RuntimeError:
			print("You have no followers...")
		except Exception as e:
			print(f"Something went wrong. Error was {e}")
			raise e


class NarcissistBot:
	"""Likes tweets based on a search content."""
	def __init__(self):
		self.api = create_twitter_api()
	
	def favorite_tweet(self, search_string: str, number_of_tweets: int) -> None:
		"""
		Uses a search string and a number of tweets to curse through tweets and like tweets containing the search string
		Args:
			search_string: The search string that you want the tweets to contain
			number_of_tweets: The number of tweets you want to like
		"""
		for tweet in limit_handle(tweepy.Cursor(self.api.search, search_string).items(number_of_tweets)):
			try:
				tweet.favorite()
				print("I liked that tweet")
			except tweepy.TweepError as e:
				print(e.reason)
			except RuntimeError:
				break

if __name__ == '__main__':
	NarcissistBot().favorite_tweet("python", 2)
