import pandas as pd
 
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from konlpy.corpus import kolaw
from konlpy.utils import pprint
 
# this is a very toy example, do not try this at home unless you want to understand the usage differences
file = open('./mujung.txt','r',encoding='utf-8')
lines = file.readlines()

# 2. 변수 okja에 전체댓글을 다시저장
docs = []
for line in lines:
    docs.append(line)
file.close()


# docs = kolaw.open('./test2.txt').read()

# docs=["the house had a tiny little mouse",
#       "the cat saw the mouse",
#       "the mouse ran away from the house",
#       "the cat finally ate the mouse",
#       "the end of the mouse story"
#      ]

print(type(docs))

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
 
 
# from sklearn.feature_extraction.text import TfidfVectorizer 
 
# # settings that you use for count vectorizer will go here
# tfidf_vectorizer=TfidfVectorizer(use_idf=True)
 
# # just send in all your docs here
# tfidf_vectorizer_vectors=tfidf_vectorizer.fit_transform(docs)

# # get the first vector out (for the first document)
# first_vector_tfidfvectorizer=tfidf_vectorizer_vectors[0]
 
# # place tf-idf values in a pandas data frame
# df = pd.DataFrame(first_vector_tfidfvectorizer.T.todense(), index=tfidf_vectorizer.get_feature_names(), columns=["tfidf"])
# df.sort_values(by=["tfidf"],ascending=False)

# tfidf_vectorizer=TfidfVectorizer(use_idf=True)
 
# # just send in all your docs here
# fitted_vectorizer=tfidf_vectorizer.fit(docs)
# tfidf_vectorizer_vectors=fitted_vectorizer.transform(docs)
