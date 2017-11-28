import tweepy
import sys



consumer_key = ' your consumer key '
consumer_secret = 'your consumer secrety'
access_token = 'your access token'
access_token_secret = 'your access token secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)
# auth.set_access_token(access_token, access_token_secret)
'''
Leave auth.set_access_token commented,
as it seems to cause error messages on some IDE's for Python 3.5/6.
'''

api = tweepy.API(auth)

sys.stdout = open("output.txt", "a+")
'''
It doesn't have to be output.txt,
you can name your text file whatever you prefer.
'''

user = api.get_user('enter the Twitter username')
print("Username: ", user.name)
print("Location: ", user.location)
print("Following: ", user.friends_count)
print("Followers: ", user.followers_count, "\n")

sys.stdout.close()

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

~~~~~~~ Credits to seo-genial.de ~~~~~~~
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
