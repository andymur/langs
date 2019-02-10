#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from germalemma import GermaLemma
import pickle
from ClassifierBasedGermanTagger.ClassifierBasedGermanTagger import ClassifierBasedGermanTagger

lemmatizer = GermaLemma()

# passing the word and the POS tag ("N" for noun)
with open('data/pos.pickle', 'rb') as f:
        tagger = pickle.load(f)

pos = tagger.tag(['Jungen', u'Wände', u'Wänden'])
print(pos)
for item in pos:
    w, p = item
    print(lemmatizer.find_lemma(w, p))
#lemma = lemmatizer.find_lemma(u'Jungen', u'N')
#print(lemma)
