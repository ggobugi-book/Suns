from sklearn.feature_extraction.text import TfidfVectorizer
from konlpy.tag import Twitter
twitter = Twitter()

file = open('./test2.txt','r',encoding='utf-8')
lines = file.readlines()

# 2. 변수 rawdata 저장
rawdata = []
for line in lines:
    rawdata.append(line)
file.close()

tfv=TfidfVectorizer(tokenizer=twitter.morphs, ngram_range=(1,2),min_df=3, max_df=0.9)
tfv.fit(rawdata)
tfv_test = tfv.transform(rawdata)
tfv_test
