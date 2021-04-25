from src.utils.helper_functions import create_twitter_api

api = create_twitter_api()

user = api.me()

public_tweets = api.home_timeline()

print("Printing my tweets")
if len(public_tweets) == 0:
    print(f"{user.screen_name} has no tweets :(")
for tweet in public_tweets:
    print(tweet.text)
    
print("Printing followers")


print(f"{user.screen_name} has {user.followers} followers")
