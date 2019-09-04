from pymongo import MongoClient
import csv

host = 'localhost'
port = 27017
user_name = 'deep'
user_password = 'Messi'
user_auth_source = 'new_db'
clinet = MongoClient(host, port, username = user_name, password = user_password, authSource = user_auth_source)

csvFile = open('search_part_3.csv', 'r')
reader = csv.DictReader(csvFile)

for row in reader:
    try:
        tweet_id = clinet.cool_db.tweets_collection.insert_one(row).inserted_id
        print('Record added: ',tweet_id)
    except:
        pass