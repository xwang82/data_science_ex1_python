import sys
import json
from collections import Counter

def keywithmaxval(d):
    """ a) create a list of the dict's keys and values; 
        b) return the key with the max value"""  
    v=list(d.values())
    k=list(d.keys())
    return k[v.index(max(v))]

def main():
    tweet_file = open(sys.argv[1],"r")

    #construct dictionary
    freqDict = {}
    #c = Counter()
  
    #parse the input tweet file
    for line in tweet_file:
            tweet = json.loads (line)
            #print tweet.keys()
            #if type(tweet["coordinates"]) == 'dict':
            #print type(tweet["place"])
            if tweet["entities"]["hashtags"]:
                for l in tweet["entities"]["hashtags"]:
                    word =  l['text']

                    #look up dictionary
                    if word in freqDict:
                        freqDict[word] += int(1)
                    else:
                        freqDict[word] = int(1)
    d = Counter(freqDict)
    for k, v in d.most_common(10):
        print k, v
    


if __name__ == '__main__':
    main()
