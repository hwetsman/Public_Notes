#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extract the sentence with the most frequently used words from a paragraph
Based on script by Aman Kharwal
added 3-10-22
Created on Thu Mar 10 09:45:16 2022
@author: howardwetsman
"""

import nltk
import string
from heapq import nlargest


def Select_Sentence(text):
    if text.count(". ") > 20:
      length = int(round(text.count(". ")/10, 0))
    else:
      length = 1
      
    nopucnt =[char for char in text if char not in string.punctuation]
    nopucnt = "".join(nopucnt)
    
    processed_text = [word for word in nopucnt.split() if word.lower() not in nltk.corpus.stopwords.words('english')]
    
    word_freq = {}
    for word in processed_text:
      word_freq[word] = 1+word_freq.get(word,0)
    
    max_freq = max(word_freq.values())
    for word in word_freq.keys():
        word_freq[word] = (word_freq[word]/max_freq)
        
    sent_list = nltk.sent_tokenize(text)
    sent_score = {}
    for sent in sent_list:
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_freq.keys():
                if sent not in sent_score.keys():
                    sent_score[sent] = word_freq[word]
                else:
                    sent_score[sent] = sent_score[sent] + word_freq[word]
    summary_sents = nlargest(length, sent_score, key=sent_score.get)
    summary = " ".join(summary_sents)
    return summary


text = nltk.corpus.gutenberg.raw('austen-emma.txt')

master_list = ['. ','.','\n','?',".'"]
for para in text.split('\n\n'):
    count = para.count('. ')+para.count('!')+para.count('?')+para.count('.\"')
    # print(para,count)
    # print('para')
    # print()
    if para.count('. ') == 0:
        print(para,'\n\n')
    else:
        sentence = Select_Sentence(para)
        print(sentence,'\n\n')
    
