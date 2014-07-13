import json
import sys

def keywithmaxval(d):
    """ a) create a list of the dict's keys and values; 
        b) return the key with the max value"""  
    v=list(d.values())
    k=list(d.keys())
    return k[v.index(max(v))]


def main():
    
    afinnfile = open(sys.argv[1],"r")
    tweet_file = open(sys.argv[2],"r")
    
    
    #construct dictionary
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
      
      
    #Dic to store states
    stateDict = {}
    statescoreDict = {}
    
    stateDict = {
    'WA':'Washington',
    'DE':'Delaware',
    'DC':'Washington DC',
    'WI':'Wisconsin',
    'WV':'West Virginia',
    'HI':'Hawaii',
    'FL':'Florida',
    'WY':'Wyoming',
    'NH':'New Hampshire',
    'NJ':'New Jersey',
    'NM':'New Mexico',
    'TX':'Texas',
    'LA':'Louisiana',
    'NC':'North Carolina',
    'ND':'North Dakota',
    'NE':'Nebraska',
    'TN':'Tennessee',
    'NY':'New York',
    'PA':'Pennsylvania',
    'CA':'California',
    'NV':'Nevada',
    'VA':'Virginia',
    'CO':'Colorado',
    'AK':'Alaska',
    'AL':'Alabama',
    'AR':'Arkansas',
    'VT':'Vermont',
    'IL':'Illinois',
    'GA':'Georgia',
    'IN':'Indiana',
    'IA':'Iowa',
    'OK':'Oklahoma',
    'AZ':'Arizona',
    'ID':'Idaho',
    'CT':'Connecticut',
    'ME':'Maine',
    'MD':'Maryland',
    'MA':'Massachusetts',
    'OH':'Ohio',
    'UT':'Utah',
    'MO':'Missouri',
    'MN':'Minnesota',
    'MI':'Michigan',
    'RI':'Rhode Island',
    'KS':'Kansas',
    'MT':'Montana',
    'MS':'Mississippi',
    'SC':'South Carolina',
    'KY':'Kentucky',
    'OR':'Oregon',
    'SD':'South Dakota'
    }
    
    
    k = stateDict.keys()
    for k in stateDict:
        #currStr = "'" + k + "'" + ":" + "'" + stateDict[k] +"'" + ","
        statescoreDict[k] = int(0)
        #print currStr
    
    
    
    for line in tweet_file:
            tweet = json.loads (line)
            #print tweet.keys()
            #if type(tweet["coordinates"]) == 'dict':
            #print type(tweet["place"])
            
            #Score the tweet
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
                        score_line += scores[word]
            #print score_line
            
            
            
            
            if tweet["place"]:
                geo_Str = tweet["place"]["full_name"].encode("utf-8")
                #print geo_Str
                
                #scan for all keys in state dict
                for k in stateDict:
                    if stateDict[k] in geo_Str:
                        statescoreDict[k]+=score_line
                    elif k in geo_Str:
                        statescoreDict[k]+=score_line

                
    """ 
    k = statescoreDict.keys()
    state_List = ["",0]
    for k in stateDict:
        #print k , statescoreDict[k]
        if statescoreDict[k] > state_List[1]:
            state_List[0] = k
            state_List[1] = statescoreDict[k]
    print state_List
    #print state_List[0]
    """
    print keywithmaxval(statescoreDict)
    tweet_file.close()

if __name__ == '__main__':
    main()