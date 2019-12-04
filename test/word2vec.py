from collections import Counter
from konlpy.tag import Kkma
from konlpy.utils import pprint
from konlpy.tag import Twitter
from konlpy.tag import Komoran
from gensim.models import word2vec
import matplotlib.pyplot as plt
import re

file = open('./test.txt','r',encoding='utf-8')
lines = file.read()

sentences = re.split('(?<=[2-9]\n)|(?<=[0-9][0-9]\n)|(?<=[0-9][0-9][0-9]\n)', lines)

sent=[]
for stuff in sentences:
        sent.append(stuff)

twitter = Twitter()

result = []
for line in sent:
    r = []
    words = twitter.pos(line,norm=True)
    for word in words:
        if word[1] not in ["Punctuation","Eomi","Josa"]:
            r.append(word[0])
            result.append(" ".join(r).strip())

data = word2vec.LineSentence(result)
model = word2vec.Word2Vec(data,
        size=200,window=10,hs=1,min_count=2,sg=1)


# model.save("toji.model")

# model = word2vec.Word2Vec.load('toji.model')
# things = model.most_similar(positive["집"])

print(list(model.wv.vocab.keys()))
# print(things) 