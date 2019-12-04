from konlpy.tag import Twitter
from gensim.models import word2vec
from bs4 import BeautifulSoup
import codecs


file = open('./test.txt','r',encoding='utf-8')
lines = file.readlines()
twitter = Twitter()
result = []
for line in lines:
    r = []
    words = twitter.pos(line,norm=True)
    for word in words:
        if word[1] not in ["Punctuation","Eomi","Josa"]:
            r.append(word[0])
    result.append(" ".join(r).strip())

fileName = "toji.wakati"

with open(fileName,'w') as fp:
    fp.write("\n".join(result))

data = word2vec.LineSentence(fileName)
model = word2vec.Word2Vec(data,
        size=200,window=10,hs=1,min_count=2,sg=1)
# size -> 200차원백터로 바꾸어주라
# window -> 주면 단어는 앞뒤로 10개
# min_count -> 출현 빈도는 2개 미만은 제외하라
# sg -> 분석 방법론은 CBOW와 Skip-Gram 둘중 후자를 선택해라
# hs -> hs가 1이면 softmax를 트레이닝할때 사용  0이면 0이 아닌경우 음수로 샘플링됩니다.
model.save("toji.model")


from gensim.models import word2vec
model = word2vec.Word2Vec.load('toji.model')
things = model.most_similar(positive["선생"])
print(things)

