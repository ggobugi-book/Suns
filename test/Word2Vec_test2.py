from collections import Counter
from konlpy.tag import Kkma
from konlpy.utils import pprint
from konlpy.tag import Twitter
from konlpy.tag import Komoran
from gensim.models import Word2Vec
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

# 1. 이전 포스트에서 크롤링한 댓글파일을 읽기전용으로 호출함
file = open('./test4.txt','r',encoding='utf-8')
lines = file.readlines()
# 2. 변수 okja에 전체댓글을 다시저장
okja = []
for line in lines:
    okja.append(line)
file.close()

twitter = Twitter()

# 4. 각 문장별로 형태소 구분하기
sentences_tag = []
for sentence in okja:
    morph = twitter.pos(sentence)
    sentences_tag.append(morph)
    # print(morph)
    # print('-'*30)


# print(sentences_tag)
# print(len(sentences_tag))
print('\n'*3)

# 5. 명사 혹은 형용사인 품사만 선별해 리스트에 담기
noun_adj_list = [] 
for sentence1 in sentences_tag:
    for word, tag in sentence1:
        if tag in ['Noun','Adjective']:
            noun_adj_list.append(word)


# 6. 선별된 품사별 빈도수 계산 & 상위 빈도 10위 까지 출력
counts = Counter(noun_adj_list)
print(counts.most_common(10))

# window크기 5, 최소 출현수 2, skip-gram, 10000번 학습
model = Word2Vec(noun_adj_list,size=200,window=10,hs=1,min_count=2,sg=1)


print(list(model.wv.vocab.keys()))
print("vocab length : %d"%len(model.wv.vocab))

print(model.wv.most_similar("몰라"))