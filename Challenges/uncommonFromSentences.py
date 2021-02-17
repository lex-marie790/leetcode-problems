"""We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words. 

You may return the list in any order.

Note:

0 <= A.length <= 200
0 <= B.length <= 200
A and B both contain only spaces and lowercase letters.

 """
"""
Understand
a = 'this apple is sweet', b = 'this apple is sour'
output: ['sweet', 'sour']

a = 'apple apple', b = 'apple'
output: []

a = 'orange pear', b = 'strawberry pineapple'
output: ['orange', 'pear','strawberry', 'pineapple' ]

Plan
Split string into list
Keep track of word occurances in both lists
sentenceA will have a dict [word --> num occurences]
sentenceB will have a dict [word --> num occurence]

To know if a word is uncommon, check if num of occurrences sentences is 1 AND it doesnt occure in sentenceB

"""


class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        wordCountInA = self.countWords(A)
        wordCountInB = self.countWords(B)
        res = []
        for (word, numOccurance) in wordCountInA.items():
            if numOccurance == 1 and word not in wordCountInB:
                res.append(word)
        for (word, numOccurance) in wordCountInB.items():
            if numOccurance == 1 and word not in wordCountInA:
                res.append(word)
        return res
    
    def countWords(self, sentence):
        wordCount = {}
        sentenceList = sentence.split(' ')
        for word in sentenceList:
            if word not in wordCount:
                wordCount[word] = 1
            else:
                wordCount[word] += 1
        return wordCount
        