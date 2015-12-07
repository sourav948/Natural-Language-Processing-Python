import nltk
import codecs
import string
import re
from nltk.corpus import stopwords
from nltk.util import bigrams

tokenFreq = {}
tokens = []

with open("microblog2011.txt", "r") as f:
    line = f.read().decode('utf8')
    tokens = nltk.word_tokenize(line)
    tokenFreq = nltk.FreqDist(tokens)

freqFile = open("Tokens.txt", "w")
freqFileWOPunc = open("freq_wo_punc.txt", "w")
freqWOStopWords = open("freq_wo_stop.txt", "w")

stopset = set(stopwords.words('english'))
oneFreqCount = 0 

for token in tokenFreq.keys():
    if tokenFreq[token] == 1:
        oneFreqCount += 1            


for token in sorted(tokenFreq, key = tokenFreq.get, reverse=True):
    freqFile.write("{}:{}\n".format(token.encode('utf8'), tokenFreq[token]))  
    if re.search('[^A-Za-z0-9_]', token) is None :
        freqFileWOPunc.write("{}:{}\n".format(token.encode('utf8'), tokenFreq[token]))
        if token not in stopset:
            freqWOStopWords.write("{}:{}\n".format(token.encode('utf8'), tokenFreq[token]))

print ("Words with freq 1 : {}".format(oneFreqCount)) 

listForBigram = []
bigramListFreq = {}
bigramList = []
bigramFile = open("bigram.txt", "w")

for token in tokens:
    if re.search('[^A-Za-z0-9_]', token) is None and token not in stopset :
        listForBigram.append(token)        
    
bigramList = list(bigrams(listForBigram))

i = 0 
for bigramTuple in bigramList:
    if bigramListFreq.has_key(bigramTuple):
        bigramListFreq[bigramTuple] = bigramListFreq[bigramTuple] + 1
    else :
        bigramListFreq[bigramTuple] = 1

for token in sorted(bigramListFreq, key = bigramListFreq.get, reverse=True):
    bigramFile.write("({},{}):{}\n".format(token[0].encode('utf8'), token[1].encode('utf8'), bigramListFreq[token]))  

freqFile.close() 
freqFileWOPunc.close()
freqWOStopWords.close()
bigramFile.close()



