import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    afinnfile = open(sys.argv[1],"r")
    tweet_file = open(sys.argv[2],"r")
    
    #construct dictionary, for known words
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.

    #list to save all sentiments for sentence
    L_sent = []

    #construct dictionary, for new words
    newword = {}
    newwordcnt = {}
    
    #parse the input tweet file to get sentence level score
    for line in tweet_file:
            tweet = json.loads (line)
            #print tweet.keys()
            score_line = 0
            
            #if the tweet has text field
            if tweet.has_key("text"):
                textline =  tweet["text"].encode("utf-8")
                wordList = textline.strip().split()
                
                #look up each word in this tweet
                for word in wordList:
                    word = word.lower()
                    word = word.strip()
                    
                    #look up dictionary
                    if word in scores:
                        score_line = score_line + scores[word]

                #look up each word in this tweet, 2nd time
                for word in wordList:
                    word = word.lower()
                    word = word.strip()
                    
                    #look up dictionary
                    if not word in scores:
                        if word in newword:
                            newword[word] += float(score_line)
                            newwordcnt[word] += 1
                        else:
                            newword[word] = float(score_line)
                            newwordcnt[word] = 1

    k = newword.keys()
    k.sort()
    for k in newword:
        #newword[word] = newword[word] / newwordcnt[word]
        print k , newword[k]




if __name__ == '__main__':
    main()
