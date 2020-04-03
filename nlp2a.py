# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 19:36:37 2020

@author: abhim
"""
#q1

import nltk
from nltk.corpus import brown

whwords = ['what', 'which', 'why', 'when', 'where', 'who']

genre_news = brown.words(categories = 'news')
fdist = nltk.FreqDist(genre_news)
count =0

for wh in whwords:
    count = count + fdist[wh]
    
print("\n", count)

#q2
categories = list(brown.categories());
modals=['can','could','may','might','must','will','would'] 

for c in categories:
    print(c)
    words=brown.words(categories=c)
    fdist=nltk.FreqDist([w.lower() for w in words])
    for m in modals:
        print( m +':',fdist[m])
    print()
    
#q3
import nltk
from nltk.corpus import inaugural
print(inaugural.fileids())
year=[fileid[:4] for fileid in inaugural.fileids()]
print(year)

#q4
cfd = nltk.ConditionalFreqDist(
  (target, fileid[:4])
  for fileid in nltk.corpus.state_union.fileids()
  for w in nltk.corpus.state_union.words(fileid)
  for target in ['men', 'women', 'people']
  if w.lower().startswith(target))
cfd.plot()

#q5
news=brown.words(categories='news')
religion=brown.words(categories='religion')

print('news',len(news))
print('religion',len(religion))

news_sents = nltk.corpus.brown.sents(categories='news')
print(float(len(news)) / len(news_sents))

religion_sents=nltk.corpus.brown.sents(categories='religion')
print(float(len(religion))/len(religion_sents))
#set is used to get length unique words
vocab_richness_news=float(len(news)/len(set(news)))

print("news  richness:",vocab_richness_news)
vocab_richness_relegion=float(len(religion)/len(set(religion)))
print("religion richness:",vocab_richness_relegion)

#q6
from nltk.probability import ConditionalFreqDist
from nltk.corpus import brown
import nltk

w = brown.words()
fdist = nltk.FreqDist(w)
ans6 = [word for word in w if fdist[word]>=3]

#q7
import pandas as pd
a7_cat=[]
a7_div=[]
for g in brown.categories():
    words=brown.words(categories=g)
    a7_cat.append(g)
    a7_div.append(float(len(set(words)))/(len(words)))

print(a7_cat[a7_div.index(min(a7_div))] )
a7 = pd.DataFrame(a7_cat,a7_div)
print(a7)

#q8
from nltk.corpus import stopwords
f = nltk.FreqDist(brown.words(categories='news'))
ans8a = f.most_common(50)

clean_words = [word for word in brown.words(categories='news') if word.isalpha()]
f = nltk.FreqDist(clean_words)
ans8b = f.most_common(50)
print(ans8b)
print()
print(clean_words[:10])
