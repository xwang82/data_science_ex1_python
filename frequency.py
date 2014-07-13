import sys
import json

def main():
    tweet_file = open(sys.argv[1],"r")

    #construct dictionary, for new words
    newwordcnt = {}
    linecnt = 0
    
    #parse the input tweet file to get sentence level score
    for line in tweet_file:
            tweet = json.loads (line)
            linecnt += 1
            
            #if the tweet has text field
            if tweet.has_key("text"):
                textline =  tweet["text"].encode("utf-8")
                wordList = textline.strip().split()
                
                #look up each word in this tweet

                #look up each word in this tweet, 2nd time
                for word in wordList:
                    word = word.lower()
                    word = word.strip()
                    
                    #look up dictionary
                    if word in newwordcnt:
                        newwordcnt[word] += float(1)
                    else:
                        newwordcnt[word] = float(1)

    k = newwordcnt.keys()
    k.sort()
    for k in newwordcnt:
        newwordcnt[k] = newwordcnt[k] / linecnt
        print k , newwordcnt[k]




if __name__ == '__main__':
    main()