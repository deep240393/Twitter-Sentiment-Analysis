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




class listener(StreamListener):

    def remove_u(self, word): #this function is used to remove emojis from tweet,name and location
        word_u = (word.encode('unicode-escape')).decode("utf-8", "strict")
        if r'\u' in word_u: 
            # print(True)
            return word_u.split('\\u')[0]
        return word

    def on_data(self, data):
		
	    listen_object = listener()
            tweet=data.split('"text":"')[1].split(',"source":"')[0]
            name=data.split(',"name":"')[1].split('","screen_name":')[0]
            name1=name.split(" ")
            name2=''
            for i in range(len(name1)):
                t=(listen_object.remove_u(name1[i]))
                name2=name2+" "+t
            name3=re.sub(r"\\","",name2)
            location=data.split(',"location":')[1].split(',"url":')[0]
            location1=location.split(" ")
            location2=''
            for i in range(len(location1)):
                l=(listen_object.remove_u(location1[i]))
                location2=location2+" "+l
            location3=re.sub(r"\\","",location2)
            timeofcreation=data.split('"created_at":"')[1].split('","id":')[0]
            tweet1 = re.sub(r"http\S+", "", tweet)
            tweet4=tweet1.split(" ")
            tweet5= ''
            for i in range(len(tweet4)):
                c=(listen_object.remove_u(tweet4[i]))
                tweet5=tweet5+" "+c
            tweet6=re.sub(r"\\n","",tweet5)
            tweet7=re.sub(r"\\","",tweet6)
            print(name2+"\n"+tweet7+"\n"+location3+"\n"+timeofcreation+"\n")
            savefile=str(time.time())+"::"+tweet7+"::"+name2+"::"+location3+"::"+timeofcreation
            save= open('stream_part4.csv','a')
            save.write(savefile)
            save.write("\n\n")
            save.close()
            return(True)
 
    def on_error(self, status):
        print (status)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Halifax"])