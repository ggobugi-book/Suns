
# sklearn / 문장 특징 추출과 유사도 측정
# 출처 : https://blog.breezymind.com/2018/03/02/sklearn-feature_extraction-text-2/


import pandas as pd
pd.options.mode.chained_assignment = None

import numpy as np
np.random.seed(0)

from konlpy.tag import Twitter
twitter = Twitter()

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity
 
# tokenizer : 문장에서 색인어 추출을 위해 명사,동사,알파벳,숫자 정도의 단어만 뽑아서 normalization, stemming 처리하도록 함
def tokenizer(raw, pos=["Noun","Alpha","Verb","Number"], stopword=[]):
    return [
        word for word, tag in twitter.pos(
            raw, 
            norm=True,   # normalize 그랰ㅋㅋ -> 그래ㅋㅋ
            stem=True    # stemming 바뀌나->바뀌다
            )
            if len(word) > 1 and tag in pos and word not in stopword
        ]



file = open('./mujung.txt','r',encoding='utf-8')
lines = file.readlines()

# 2. 변수 rawdata 저장
rawdata = []
for line in lines:
    rawdata.append(line)
file.close()

# rawdata = [
#     '남북 고위급회담 대표단 확정..남북 해빙모드 급물살',
#     '[남북 고위급 회담]장차관만 6명..판 커지는 올림픽 회담',
    
#     '문재인 대통령과 대통령의 영부인 김정숙여사 내외의 동반 1987 관람 후 인터뷰',
#     '1987 본 문 대통령.."그런다고 바뀌나? 함께 하면 바뀐다"',
    
#     '이명박 전 대통령과 전 대통령의 부인 김윤옥 여사, 그리고 전 대통령의 아들 이시형씨의 동반 검찰출석이 기대됨'
# ]

vectorize = CountVectorizer(
    tokenizer = tokenizer,
    min_df=2
                # 예제로 보기 좋게 1번 정도만 노출되는 단어들은 무시하기로 했다
                # min_df = 0.01 : 문서의 1% 미만으로 나타나는 단어 무시
                # min_df = 10 : 문서에 10개 미만으로 나타나는 단어 무시
                # max_df = 0.80 : 문서의 80% 이상에 나타나는 단어 무시
                # max_df = 10 : 10개 이상의 문서에 나타나는 단어 무시
)

X = vectorize.fit_transform(rawdata)

print(
    'fit_transform, (sentence {}, feature {})'.format(X.shape[0], X.shape[1])
)

print(type(X))

print(X.toarray())

# 문장에서 뽑아낸 feature 들의 배열
features = vectorize.get_feature_names()

# 검색 문장에서 feature를 뽑아냄
srch=[t for t in tokenizer('형식') if t in features]
print(srch)
# ['1987', '대통령']
 
# dtm 에서 검색하고자 하는 feature만 뽑아낸다.
srch_dtm = np.asarray(X.toarray())[:, [
    # vectorize.vocabulary_.get 는 특정 feature 가 dtm 에서 가지고 있는 index값을 리턴한다
    vectorize.vocabulary_.get(i) for i in srch
]]

score = srch_dtm.sum(axis=1)
print(score)
# array([0, 0, 3, 2, 3], dtype=int64) 문장별 feature 합계 점수
 
for i in score.argsort()[::-1]:
    if score[i] > 0:
        print('{} / score : {}'.format(rawdata[i], score[i]))
        


####################

vectorize = TfidfVectorizer(
    tokenizer=tokenizer,
    min_df=2,
    
    sublinear_tf=True    # tf값에 1+log(tf)를 적용하여 tf값이 무한정 커지는 것을 막음
)
X = vectorize.fit_transform(rawdata)
 
print(
    'fit_transform, (sentence {}, feature {})'.format(X.shape[0], X.shape[1])
)
# fit_transform, (sentence 5, feature 7)
 
print(X.toarray())
 
# ([[0.        , 0.40824829, 0.81649658, 0.        , 0.        , 0.        , 0.40824829],
# [0.        , 0.40824829, 0.40824829, 0.        , 0.        , 0.        , 0.81649658],
# [0.41680418, 0.        , 0.        , 0.69197025, 0.41680418, 0.41680418, 0.        ],
# [0.76944707, 0.        , 0.        , 0.63871058, 0.        , 0.        , 0.        ],
# [0.        , 0.        , 0.        , 0.8695635 , 0.34918428, 0.34918428, 0.        ]])
 
# 문장에서 뽑아낸 feature 들의 배열
features = vectorize.get_feature_names()
# 검색 문장에서 feature를 뽑아냄
srch=[t for t in tokenizer('젊은 느티나무') if t in features]
print(srch)
# ['1987', '대통령']
 
# dtm 에서 검색하고자 하는 feature만 뽑아낸다.
srch_dtm = np.asarray(X.toarray())[:, [
    # vectorize.vocabulary_.get 는 특정 feature 가 dtm 에서 가지고 있는 index값을 리턴한다
    vectorize.vocabulary_.get(i) for i in srch
]]
 
#       1987    대통령
# 0     0.000000    0.000000
# 1     0.000000    0.000000
# 2     0.416804    0.691970
# 3     0.769447    0.638711
# 4     0.000000    0.869563
 
score = srch_dtm.sum(axis=1)
print(score)
# array([0.         0.         1.10877443 1.40815765 0.8695635 ], dtype=int64) 문장별 feature 합계 점수
 
for i in score.argsort()[::-1]:
    if score[i] > 0:
        print('{} / score : {}'.format(rawdata[i], score[i]))
 
# 1987 본 문 대통령.."그런다고 바뀌나? 함께 하면 바뀐다" / score : 1.408157650537996
# 문재인 대통령과 대통령의 영부인 김정숙여사 내외의 동반 1987 관람 후 인터뷰 / score : 1.1087744279177436
# 이명박 전 대통령과 전 대통령의 부인 김윤옥 여사, 그리고 전 대통령의 아들 이시형씨의 동반 검찰출석이 기대됨 / score : 0.869563495264799



################ HashingVecorizer
vectorize = HashingVectorizer(
    tokenizer=tokenizer,
    n_features=7               # 기본 feature 수를 설정하며 기본값이 2의 20승이다. 아래 예시를 위해 feature 를 7로 한정했으나, 아래 유사문장을 찾을때는 다시 n_features 주석처리 했다.
)
X = vectorize.fit_transform(rawdata)
 
print(X.shape)
# (5, 7)
 
print(X.toarray())
 
# ([[ 0.33333333,  0.33333333, -0.33333333,  0.33333333,  0.33333333, 0.66666667,  0.        ],
# [ 0.        ,  0.        , -0.57735027,  0.57735027,  0.57735027, 0.        ,  0.        ],
# [ 0.        ,  0.        ,  0.        ,  0.        , -0.21821789, -0.43643578,  0.87287156],
# [ 0.        ,  0.        ,  0.        ,  0.81649658,  0.        , -0.40824829,  0.40824829],
# [ 0.28867513,  0.28867513, -0.28867513,  0.28867513, -0.57735027, 0.        ,  0.57735027]])

# search 문장 벡터
srch_vector = vectorize.transform([
    '젊은 느티나무'
])
 
print(srch_vector.shape)
# (1, 7)

from sklearn.metrics.pairwise import linear_kernel
 
# linear_kernel는 두 벡터의 dot product 이다.
cosine_similar = linear_kernel(srch_vector, X).flatten()
# cosine_similar = (srch_vector*X.T).toarray().flatten()
 
print(cosine_similar)
# [0.         0.         0.62017367 0.31622777 0.3]
 
print(cosine_similar.shape)
# (5,)
 
# 유사한 rawdata index
sim_rank_idx = cosine_similar.argsort()[::-1]
print(sim_rank_idx)
#[2 3 4 1 0]
 
for i in sim_rank_idx:
    if cosine_similar[i] > 0:
        print('{} / score : {}'.format(rawdata[i], cosine_similar[i]))
 
# 문재인 대통령과 대통령의 영부인 김정숙여사 내외의 동반 1987 관람 후 인터뷰 / score : 0.6201736729460423
# 1987 본 문 대통령.."그런다고 바뀌나? 함께 하면 바뀐다" / score : 0.3162277660168379
# 이명박 전 대통령과 전 대통령의 부인 김윤옥 여사, 그리고 전 대통령의 아들 이시형씨의 동반 검찰출석이 기대됨 / score : 0.3