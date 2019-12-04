from collections import Counter
from konlpy.tag import Kkma
from konlpy.utils import pprint
from konlpy.tag import Twitter
from konlpy.tag import Komoran
from gensim.models import Word2Vec
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import re

file = open('./mujung.txt','r',encoding='utf-8')
lines = file.read()

sentences = re.split('(?<=[0-9]\n)|(?<=[0-9][0-9]\n)|(?<=[0-9][0-9][0-9]\n)', lines)

sent=[]
for stuff in sentences:
        sent.append(stuff)


twitter = Twitter()

sentences_tag = []
for sentence in sent:
    morph = twitter.pos(sentence)
    sentences_tag.append(morph)
