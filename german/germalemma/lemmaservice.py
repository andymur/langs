# -*- coding: utf-8 -*-
from germalemma import GermaLemma
import pickle
from ClassifierBasedGermanTagger.ClassifierBasedGermanTagger import ClassifierBasedGermanTagger
from flask import Flask
app = Flask(__name__)

lemmatizer = GermaLemma()

with open('data/pos.pickle', 'rb') as f:
        tagger = pickle.load(f)

@app.route('/')
def hello_world():
    pos = tagger.tag(['Wand', u'Wände', u'Wänden'])
    print(pos)
    for item in pos:
        w, p = item
        print(lemmatizer.find_lemma(w, p))
    return 'Hello, World!'
