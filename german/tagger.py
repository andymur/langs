import nltk
import pickle

if __name__ == "__main__":
    with open('nltk_german_classifier_data.pickle', 'rb') as f:
        tagger = pickle.load(f)
    print(tagger.tag(['spielt', 'Tisch']))
