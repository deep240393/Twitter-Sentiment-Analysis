# Twitter-Sentiment-Analysis
# Assignment 2

## Sentiment Analysis on Twitter Posts

1.  Introduction
2.  Tweet Extraction
3.  Sentiment Analysis
4.  Create MapReduce Program

----------

###### Introduction

In this problem, set of tweets is to be extracted from the twitter database and then sentiment analysis is performed on it, in order to find polarity (positive, negative or neutral emotion) of the tweets. Finally, MapReduce is imlemented using Apache Spark to find out frequency of particular words.

###### Setup of Apache Spark:

• We need to create a new EC2 instance with inbound port 8080, and 8081 enabled.
• As Apache spark require java installation, we need to add java PPA to apt run, install Oracle as well as python.
• After creating a server folder on the cloud, we can download Apache spark and unpack it.
• We need to export JAVA_HOME, SPARK_HOME and python 3 and append it into the .profile file.
• We need to start Master and Slave and ensure that JAVA_HOME is properly setup.
➔spark-root-org.apache.spark.deploy.master.Master-1-ip-172-31-16-68.out (master)
➔sudo ./spark-2.4.0-bin-hadoop2.7/sbin/start-slave.sh spark://ip-172-31-16-68.us-east-2.compute.internal:7077 (slave)
• By running sudo ./spark-2.4.0-bin-hadoop2.7/bin/pyspark command we can start new spark session.

###### Tweet Extraction

Tweet can be extraxted in the following order:

1.  Connecting to the twitter API
2.  Authentication
3.  Saving tweets to csv


###### Sentiment Analysis

As tweets are unstructured form of data, it needs to be preprocessed before analysing. Preprocessing is done in many phases : 
• Remove html links from the tweets 
• Remove retweet entities 
• Remove all hashtags 
• Remove all @people
• Remove all punctuation 
• Remove all numbers
• Remove all unnecessary white spaces  
• Convert all text into lowercase and 
• Remove duplicates


Sentiment Analysis is also performed in phases, algorithm can be devised as:

1.  Start with downloading and caching the sentiment dictionary
2.  Download twitter testing data sets, input it in to the program
3.  Clean the tweets by removing the stop words
4.  Tokenize each word in the dataset and feed in to the program
5.  For each word, compare it with positive sentiments and negative sentiments word in the dictionary. Then increment positive count or negative count
6.  Finally, based on the positive count and negative count, we can get result percentage about sentiment to decide the polarity

###### Data file:-
• The result of search and stream of tweets is stored in the CSV format. (ex. search.csv and stream.csv)
• For mapreduce program I have used input file in the .txt format and result of the output is stored in the map_reduce_op_stream1.txt (for 1st streaming) and map_reduce_op_stream2.txt (for 2nd streaming)
• I have created a separate folder where I have provided all the necessary screenshot related to this assignment.
