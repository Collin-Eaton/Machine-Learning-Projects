# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 22:38:13 2021

@author: Collin
"""

import os
os.chdir(r"C:\Users\Collin\Documents\collins documents\Regis Homework\Data Analytics wk 6")

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

f = open('Macbeth.txt', encoding="utf8").read()
import operator, time, string
import re
start = time.time()
book = {}

f= f.lower()

book = f

book[:50]
book = re.split(r'\W+', book)
book[:50]

stop = stopwords.words('english')
book = [ j for j in book if j not in stop]
book[:50]

remove_list = ['gutenberg', 'ebook', 'www', 'online']
book = [ j for j in book if j not in remove_list]
book[:50]

translator = str.maketrans('', '', string.punctuation) 

new_book = {}
for new_word in book:
    if new_word in new_book:
        new_book[new_word] += 1
    else:
        new_book[new_word] = 1
sorted_new_book = sorted(new_book.items(), key=operator.itemgetter(1), reverse =
True)
print('Number of distinct words: ', len(sorted_new_book))
npopular = 50
x = range(npopular)
y = []
for pair in range(npopular):
    y=y + [sorted_new_book[pair][1]]
    print(sorted_new_book[pair])