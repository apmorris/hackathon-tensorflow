import tweepy #https://github.com/tweepy/tweepy
import pandas as pd


#Twitter API credentials
consumer_key = "b9glmyLpVzNp9p702saTE8PJX"
consumer_secret = "KE86Y4na2kwKAi9xoiziv95v2ZVwFc4wWLbzjfjysd7AmSa75K"
access_key = "871714486733996032-jWhoDmXogvvYCaTZZrhBsdVgvaLiSGr"
access_secret = "CMr6SwbK5pK9M69DdBfBFdDM0lZoNTR0peBNEPI8ipHZu"

def get_all_tweets(screen_name):
    #Twitter only allows access to a users most recent 3240 tweets with this method

    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    #initialize a list to hold all the tweepy Tweets
    alltweets = []
    outtweets = []

    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=200,include_rts=False)

    #save most recent tweets
    alltweets.extend(new_tweets)

    #save the id of the oldest tweet less one
#    oldest = alltweets[-1].id - 1


    for tweet in alltweets:
        temp = tweet.text.encode("utf-8")
        outtweets.append(temp)

    return outtweets