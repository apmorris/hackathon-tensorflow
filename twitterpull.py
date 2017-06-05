#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv
import pandas as pd

#Twitter API credentials
consumer_key = "b9glmyLpVzNp9p702saTE8PJX"
consumer_secret = "KE86Y4na2kwKAi9xoiziv95v2ZVwFc4wWLbzjfjysd7AmSa75K"
access_key = "871714486733996032-jWhoDmXogvvYCaTZZrhBsdVgvaLiSGr"
access_secret = "CMr6SwbK5pK9M69DdBfBFdDM0lZoNTR0peBNEPI8ipHZu"

df = pd.read_csv('mpdata.csv')

twitterHandles = []
twitterParty = []

for elem in df.TWITTER:
    elem = elem.translate(None, '@')
    twitterHandles.append(elem)

for elem in df.CONSTITUENCY:
    twitterParty.append(elem)

def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0 and len(alltweets) < 200:
		print "getting tweets before %s" % (oldest)
		
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		
		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
		print "...%s tweets downloaded so far" % (len(alltweets))
	
	#transform the tweepy tweets into a 2D array that will populate the csv	
#	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]

        outtweets = [[tweet.text.encode("utf-8")] for tweet in alltweets]
	
	#write the csv	
	with open('%s.csv' % screen_name, 'wb') as f:
		writer = csv.writer(f)
#		writer.writerow(["id","created_at","text"])
		writer.writerows(outtweets)
	
	pass

if __name__ == '__main__':

    for elem in twitterHandles[:2]:
        print elem

        #pass in the username of the account you want to download
        get_all_tweets(elem)
