import csv
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import re

auth = tweepy.OAuthHandler("aqZfdNPXQKPGmOTtQW7LqnLuO","FzTfw6Edd3RnvSelBw7ttwITgUDMoH90l7HZtVbmTIiUUCmDHK")
auth.set_access_token ( "296112287-Kmn5Wys8hPWNS4JSeerDh5J1apC5DmmulH7ormdd" , "leai9NKqXsR8yjcbQvJIGpkL155FhQ8LwgS1701g2JAHt")
api = tweepy.API(auth)

def remove_u(word): # this function is used to remove emoticons from the tweet
    word_u = (word.encode('unicode-escape')).decode("utf-8", "strict")
    if r'\u' in word_u: 
        # print(True)
        return word_u.split('\\u')[0]
    return word

    
public_tweets=tweepy.Cursor(api.search, q="Halifax").items(700)
with open('search_part_3.csv','a') as csvfile:
    fieldnames = ['name','loc','tweet','time','rt','rt_name']
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()
    
    count=0
    rcount=0
    
    for tweet in public_tweets:
        tweet_text=(tweet.text.encode('unicode-escape')).decode("utf-8", "strict")
        tweet1 = re.sub(r"http\S+", "", tweet_text)
        tweet2=tweet1.split(" ")
        tweet3= ''
        for i in range(len(tweet2)):
            tt=(remove_u(tweet2[i]))
            tweet3=tweet3+" "+tt
        tweet4=re.sub(r"\\n","",tweet3) # used to remove new line character
        tweet5=re.sub(r"\\","",tweet4) # to remove \ from the tweet
        tweet6 = ''.join([c for c in tweet5 if ord(c) < 128])
        uname1=(tweet.user.name.encode('unicode-escape')).decode("utf-8", "strict")
        uname2=uname1.split(" ")
        uname3= ''
        for i in range(len(uname2)):
            u=(remove_u(uname2[i]))
            uname3=uname3+" "+u
        uname4=re.sub(r"\\","",uname3)
        uname5= ''.join([c for c in uname4 if ord(c) < 128])
        loc1= (tweet.user.location.encode('unicode-escape')).decode("utf-8", "strict")
        loc2=loc1.split(" ")
        loc3= ''
        for i in range(len(loc2)):
            l=(remove_u(loc2[i]))
            loc3=loc3+" "+l
        loc4=re.sub(r"\\","",loc3)		
        if hasattr(tweet,"quoted_status"):
            retweet1= re.sub(r"http\S+", "", (tweet.quoted_status.text.encode('unicode-escape')).decode("utf-8", "strict")) # captured the retweet
            retweet2=retweet1.split(" ")
            retweet3= ''
            for i in range(len(retweet2)):
            	rtt=(remove_u(retweet2[i]))
            	retweet3=retweet3+" "+rtt
            retweet4=re.sub(r"\\n","",retweet3) # used to remove new line character
            retweet5=re.sub(r"\\","",retweet4) # to remove \ from the tweet
            retweet_name= tweet.quoted_status.created_at # captured the retweet time
            tweet_dict= {'name': uname5, 'loc' :loc4, 'tweet':tweet6 ,'time': tweet.created_at,'rt':retweet5,'rt_name':retweet_name}
            writer.writerow(tweet_dict)
	    empty_dict = {'name': '', 'loc' :'', 'tweet':'' ,'time': '','rt':'','rt_name':''}
	    writer.writerow(empty_dict)
            rcount=rcount+1 # provide the count of number of retweets
        else:
            tweet_dict= {'name': uname5, 'loc' :loc4,'tweet':tweet6,'time': tweet.created_at}
            empty_dict1 = {'name': '', 'loc' :'', 'tweet':'' ,'time': ''}
            writer.writerow(tweet_dict)
	    writer.writerow(empty_dict1)
            count=count+1   # gives the count of number of tweets
    print('Total number of tweets are',count)
    print('Total number of rtweets are',rcount)