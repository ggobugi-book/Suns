from collections import Counter
from konlpy.tag import Kkma
from konlpy.utils import pprint
from konlpy.tag import Twitter
import pandas as pd
 
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from konlpy.corpus import kolaw

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
    print(morph)
    print('-'*30)

print(sentences_tag)
print(len(sentences_tag))
print('\n'*3)

# 5. 명사 혹은 형용사인 품사만 선별해 리스트에 담기
docs = [] 
for sentence1 in sentences_tag:
    for word, tag in sentence1:
        if tag in ['Noun','Adjective']:
            docs.append(word)


counts = Counter(docs)
print(counts.most_common(10))

#instantiate CountVectorizer()
cv=CountVectorizer()
 
# this steps generates word counts for the words in your docs
word_count_vector=cv.fit_transform(docs)

word_count_vector.shape

tfidf_transformer=TfidfTransformer(smooth_idf=True,use_idf=True)
tfidf_transformer.fit(word_count_vector)


# print idf values
df_idf = pd.DataFrame(tfidf_transformer.idf_, index=cv.get_feature_names(),columns=["idf_weights"])
 
# sort ascending
pprint(df_idf.sort_values(by=['idf_weights']))




# count matrix
count_vector=cv.transform(docs)
 
# tf-idf scores
tf_idf_vector=tfidf_transformer.transform(count_vector)
feature_names = cv.get_feature_names()
 
#get tfidf vector for first document
first_document_vector=tf_idf_vector[0]
 
#print the scores
df = pd.DataFrame(first_document_vector.T.todense(), index=feature_names, columns=["tfidf"])
pprint(df.sort_values(by=["tfidf"],ascending=False))
 
 