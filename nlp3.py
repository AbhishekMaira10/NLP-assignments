# -*- coding: utf-8 -*-
"""
Created on Fri Apr 5 22:49:37 2020

@author: Abhishek Maira
"""
import nltk
import matplotlib
nltk.download()
from nltk.book import *
from nltk.corpus import *
from nltk.corpus import wordnet as wn

#Q1
m = names.words('male.txt')
f = names.words('female.txt')
ambiguous=[value for value in m if value in f] 
ambiguous

#Q3
cfd = nltk.ConditionalFreqDist(
             (fileid, name[0])
             for fileid in names.fileids()
             for name in names.words(fileid))
cfd.plot()

#Q4
def supergloss(s):
    n = 0
    synset = (s.name, s.definition)
    hypernyms = s.hypernyms()
    hyponyms = s.hyponyms()
    if hypernyms != []:
        while n < len(hypernyms):
            for hypernym in s.hypernyms():
                hypernyms[n] = (hypernym.name, hypernym.definition)
                n = n + 1
    else:
        hypernyms = 'none'
    n = 0
    if hyponyms != []:
        while n < len(hyponyms):
            for hyponym in hyponyms:
                hyponyms[n] = (hyponym.name, hyponym.definition)
                n = n + 1
    else:
        hyponyms = 'none'
    total = 'ROOT WORD:', synset, 'HYPERNYMS:', hypernyms, 'HYPONYMS:', hyponyms
    return total

#Q5
poly_nouns = list(wn.all_synsets('n'))
poly_verbs = list(wn.all_synsets('v'))
#poly_adjectives = list(wn.all_synsets('adj'))
#poly_adverbs = list(wn.all_synsets('adv'))
def calc_words(synset):
	all_words = []
	for syn in synset:
		all_words += syn.lemma_names()
	total = len(set(all_words))
	return total
def total_senses(synset):
	senses = sum(1 for x in synset)
	return senses
def average_polysemy(synset):
	average = total_senses(synset) / calc_words(synset)
	return average
print(average_polysemy(poly_nouns))
print(average_polysemy(poly_verbs))
