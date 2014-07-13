#import urllib
import json
import csv

#tweet_file = open("output.json","r")
tweet_file = open("clean.json","r")
#poly_file = open("poly.py","r")
#outfile = open("clean.json","w")


#Dic to store states
stateDict = {}
statescoreDict = {}


#fObj = open("state_table.csv","r")
#csvReader = csv.reader(fObj)

#for row in csvReader:
    #print row[1]
    #print row[2]
    #stateDict[row[2]] = row[1]
    #statescoreDict[row[2]] = int(0)
#fObj.close()

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

#for line in poly_file:
        #stateloc = json.loads (line)
        #print stateloc.keys()
        #print type(stateloc['TX'])
        #for c in stateloc['TX']:
        #    print c
        #    tempTuple = (float(c['x']), float(c['y']))
        #    polygon.append(tempTuple)
        


for line in tweet_file:
        tweet = json.loads (line)
        #print tweet.keys()
        #if type(tweet["coordinates"]) == 'dict':
        #print type(tweet["place"])
        if tweet["entities"]["hashtags"]:
            for l in tweet["entities"]["hashtags"]:
                print l
                print l['text']
            
            


            

#k = statescoreDict.keys()
#for k in stateDict:
#    print k , statescoreDict[k]

tweet_file.close()
#poly_file.close()