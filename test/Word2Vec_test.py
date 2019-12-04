from collections import Counter
from konlpy.tag import Kkma
from konlpy.utils import pprint
from konlpy.tag import Twitter
from konlpy.tag import Komoran
from gensim.models import Word2Vec
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA



# 1. 이전 포스트에서 크롤링한 댓글파일을 읽기전용으로 호출함
file = open('./mujung.txt','r',encoding='utf-8')
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
    morph = twitter.nouns(sentence)
    sentences_tag.append(morph)
    print(morph)
    print('-'*30)

print(sentences_tag)
print(len(sentences_tag))
print('\n'*3)

# 5. 명사 혹은 형용사인 품사만 선별해 리스트에 담기
# sentence = [] 
# for sentence1 in sentences_tag:
#     for word, tag in sentence1:
#         if tag in ['Noun','Adjective']:
#             sentence.append(word)


# 6. 선별된 품사별 빈도수 계산 & 상위 빈도 10위 까지 출력
# counts = Counter(sentence)
# print(counts.most_common(10))





def plot_2d_praph(vocabs, xs, ys):
    plt.figure(figsize=(8,6))
    plt.scatter(xs,ys, marker = 'o')
    for i, v in enumerate(vocabs):
        plt.annotate(v, xy=(xs[i],ys[i]))



model = Word2Vec(sentence, size=300, window=3, min_count=1, workers=1)

word_vectors = model.wv

vocabs = word_vectors.vocab.keys()
word_vectors_list = [word_vectors[v] for v in vocabs]
print(word_vectors.similarity(w1='형식', w2='영채'))


pca = PCA(n_components=2)
xys= pca.fit_transform(word_vectors_list)
xs = xys[:,0]
ys= xys[:,1]
plot_2d_praph(vocabs, xs, ys)