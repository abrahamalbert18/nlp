from nltk.book import *

def lexical_diversity(text):
    return len(set(text))/len(text)
