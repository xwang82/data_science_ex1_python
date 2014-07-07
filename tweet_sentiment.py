import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    afinnfile = open(sys.argv[1],"r")
    tweet_file = open(sys.argv[2],"r")
    #hw()

    #construct dictionary
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.
    
    #parse the input tweet file
    for line in tweet_file:
            tweet = json.loads (line)
            #print tweet.keys()
            score_line = 0
            
            #if the tweet has text field
            if tweet.has_key("text"):
                textline =  tweet["text"]
                wordList = textline.strip().split()
                
                #look up each word in this tweet
                for word in wordList:
                    word = word.lower()
                    word = word.strip()
                    
                    #look up dictionary
                    if word in scores:
                        score_line = score_line + scores[word]
            print score_line


if __name__ == '__main__':
    main()
