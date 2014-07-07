#import urllib
import json

#tweet_file = open("output.json","r")
tweet_file = open("clean.json","r")
#outfile = open("clean.json","w")

for line in tweet_file:
        tweet = json.loads (line)
        #print tweet.keys()
        #if tweet.has_key("text"):
        print tweet["text"]
            #outfile.write(line)


tweet_file.close()
#outfile.close()