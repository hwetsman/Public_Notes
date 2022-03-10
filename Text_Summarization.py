"""
Based on script by Aman Kharwal
added 3-10-22
"""

import nltk
import string
from heapq import nlargest


text = "Enter Text to Summarize"

if text.count(". ") > 20:
  length = int(round(text.count(". ")/10, 0))
else:
  length = 1
  
nopucnt =[char for char in text if char not in string.punctuation]
nopucnt = "".join(nopucnt)

processed_text = [word for word in nopucnt.split() if word.lower() not in nltk.corpus.stopwords.words('english')]

word_freq = {}
for word in processed_text:
  if word not in word_freq:
    word_freq[word] = 1
  else:
    word_freq[word] = word_freq[word] + 1
 
# for word in processed_text:
#   word_freq[word] = 1+word_freq.get(word,0)

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
print(summary)
