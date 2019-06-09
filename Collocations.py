import nltk
from nltk import word_tokenize
from nltk import ngrams
from collections import Counter, OrderedDict
import string

import pandas as p
from collections import defaultdict
import math
import sys

bigramsCount = []
unigramsCount = []


def CollPMI(dirRead):
    
    
    data = dirRead.read()
    dirRead.close()
    
    token = nltk.word_tokenize(data)
    newtoken = [w.lower() for w in token if w.isalpha()]
    #print(newtoken)
    unigrams = ngrams(newtoken,1)
    bigrams = ngrams(newtoken,2)

    unigramsCount = Counter(unigrams)
    #totalCount = sum(unigramsCount.values())
    #print(totalCount)
    bigramsCount = Counter(bigrams)
    
    unigramFreq = dict()
    bigramFreq = dict()
    bigramPMI = dict()
    unisumcount =0
    for utple in unigramsCount:
       # print( utple[0] + ' ' + str( unigramsCount[utple]))
        unisumcount =  unisumcount + unigramsCount[utple]
        unigramFreq[utple[0]] = unigramsCount[utple]
        
    bisumcount=0
    for btple in bigramsCount:
        #print( btple[0] + ' ' + btple[1] + ' ' + str( bigramsCount[btple]))
        bigramFreq[btple[0] + '_' + btple[1]] = bigramsCount[btple]    
        bisumcount = bisumcount + bigramsCount[btple]
 
    for btple1 in bigramsCount:
        #print( btple[0] + ' ' + btple[1] + ' ' + str( bigramsCount[btple]))
        bigramPMI[btple1[0] + '_' + btple1[1]] =  pmi(btple1[0],btple1[1],unigramFreq,bigramFreq, unisumcount,bisumcount)
    
    revSortedPMI = sorted(bigramPMI.items() ,reverse = True, key=lambda t : t[1])
    reversePMI = Counter(revSortedPMI).most_common(20)
    
    
    for key in reversePMI:
        print(key[0][0].replace('_',' ') + ' ' + str(key[0][1]) )
    
def CollCHI(dirRead):
    
    
    data = dirRead.read()
    dirRead.close()
    
    token = nltk.word_tokenize(data)
    newtoken = [w.lower() for w in token if w.isalpha()]
    #print(newtoken)
    unigrams = ngrams(newtoken,1)
    bigrams = ngrams(newtoken,2)

    unigramsCount = Counter(unigrams)
    #totalCount = sum(unigramsCount.values())
    #print(totalCount)
    bigramsCount = Counter(bigrams)
    
    unigramFreq = dict()
    bigramFreq = dict()
    bigramWord1Freq = dict()
    bigramWord2Freq = dict()
    bigramChiSqare = dict()
    unisumcount =0
    for utple in unigramsCount:
       # print( utple[0] + ' ' + str( unigramsCount[utple]))
        unisumcount =  unisumcount + unigramsCount[utple]
        unigramFreq[utple[0]] = unigramsCount[utple]
        
    bisumcount=0
    for btple in bigramsCount:
        #print( btple[0] + ' ' + btple[1] + ' ' + str( bigramsCount[btple]))
        bigramFreq[btple[0] + '_' + btple[1]] = bigramsCount[btple]
        
        if btple[1] in bigramWord2Freq:
            bigramWord2Freq[btple[1]] = bigramWord2Freq[btple[1]] + bigramsCount[btple]
        else:
            bigramWord2Freq[btple[1]] = bigramsCount[btple]

        if btple[0] in bigramWord1Freq:
            bigramWord1Freq[btple[0]] = bigramWord1Freq[btple[0]] + bigramsCount[btple]
        else:
            bigramWord1Freq[btple[0]] = bigramsCount[btple]
        
        bisumcount = bisumcount + bigramsCount[btple]
 
    for btple1 in bigramsCount:
        #print( btple[0] + ' ' + btple[1] + ' ' + str( bigramsCount[btple]))
        bigramChiSqare[btple1[0] + '_' + btple1[1]] = chisq(bigramWord1Freq[btple[0]],bigramWord2Freq[btple[1]],bigramFreq[btple1[0] + '_' + btple1[1]],bisumcount)
    
    
    revSortedchisq = sorted(bigramChiSqare.items() ,reverse = True, key=lambda t : t[1])
    reverseChiSquare = Counter(revSortedchisq).most_common(20)
    for key in reverseChiSquare:
        print(key[0][0].replace('_',' ') + ' ' + str(key[0][1]) )


def pmi(word1, word2, unigram_freq, bigram_freq,uniTotal,biTotal):
    prob_word1 = unigram_freq[word1] / uniTotal
    prob_word2 = unigram_freq[word2] / uniTotal
    prob_word1_word2 = bigram_freq[word1 + '_' + word2] / biTotal
    return math.log(prob_word1_word2/float(prob_word1*prob_word2),2)

def chisq(bigram_word1,bigram_word2,bigram_freq,biTotal):
    observed_value =  bigram_freq
    estimated_value = (bigram_word1/biTotal)* (bigram_word2/biTotal)* biTotal
    return ((observed_value-estimated_value)**2)/estimated_value

       
def main():
    measure = sys.argv[2]
    
    filename = sys.argv[1]
    
    dirRead = open(filename)
    if measure == "PMI":
        CollPMI(dirRead)
    elif measure == "CHI":
        CollCHI(dirRead)
    else:
        print("unknown measure")

if __name__ == "__main__":
    main()     


    