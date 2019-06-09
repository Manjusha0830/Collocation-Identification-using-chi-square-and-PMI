# NLP Collocation-Identification-using-chi-square-and-PMI

Python program Collocations.py that identifies collocations in text. Specifically, your program will have to implement the chi-square and the pointwise mutual information (PMI) measures of association for the identification of bigram collocations. Run your program on  a subset of the Treebank corpus.

Programming guidelines:
➢	Collect the raw counts from the corpus for all the unigrams (individual words) and bigrams (sequences of two words). Unigrams and bigrams that include tokens consisting only of punctuation should not be included, i.e., you should not collect counts for “,” (unigram) or for “today ,” (bigram). You should instead collect counts for e.g., “U.S.” or “34.7”, where the punctuation is part of the word.
 
➢	Implement the chi-square and the PMI measures as two separate functions. Each of the two functions should use the raw counts from before, and calculate the chi-square (or PMI) for all the bigrams in the corpus. Again, bigrams that include punctuation as a separate token should not be included.
➢	Rank the bigrams in reverse order of their chisquare (or PMI) score, and output the top 20 bigrams.

The Collocations.py program should be run using a command like this:
% python Collocations.py Collocations <measure>

where the <measure> parameter could be either “chi-square” or “PMI”. Depending on  the  parameter provided in the command line, one of the two measures should be used.
Your program should produce the following output: Bigram1 Score1
Bigram2 Score2
…
Bigram20 Score20

representing the top 20 bigrams in reverse order of their chi-square (PMI) score.
