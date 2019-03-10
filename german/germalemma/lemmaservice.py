# -*- coding: utf-8 -*-
from germalemma import GermaLemma
import json
from flask import request, Response
import pickle
from ClassifierBasedGermanTagger.ClassifierBasedGermanTagger import ClassifierBasedGermanTagger
from flask import Flask
from pattern.de import singularize, conjugate, predicative

app = Flask(__name__)

lemmatizer = GermaLemma()

with open('data/pos.pickle', 'rb') as f:
        tagger = pickle.load(f)

@app.route('/normalize/<word>')
def hello_world(word):
    pos = tagger.tag([word])
    print(pos)
    content = []
    for item in pos:
        w, p = item
        lemma = lemmatizer.find_lemma(w, p)
        content.append(lemma)

    response = Response(response=json.dumps(content), status=200, mimetype='application/json')    
    return response
