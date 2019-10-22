import pickle

from keras.preprocessing import sequence
from keras.preprocessing.text import Tokenizer
from sklearn.cluster import KMeans
from sklearn.decomposition import NMF, LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import adjusted_rand_score

documents = [
    "This little kitty came to play when I was eating at a restaurant.",
    "Merly has the best squooshy kitten belly.",
    "Google Translate app is incredible",
    "If you open 100 tab in google you get a smiley face.",
    "Best cat photo I've ever taken.",
    "Climbing ninja cat.",
    "Impressed with google map feedback.",
    "Key promoter extension for Google Chrome.",
]

vectorizer = TfidfVectorizer(stop_words="english")
tfidf = vectorizer.fit_transform(documents)
feature_names = vectorizer.get_feature_names()


n_topics = 2
nmf = NMF(n_components=n_topics, random_state=1).fit(tfidf)
W = nmf.fit_transform(tfidf)

H = nmf.components_

n_top_words = 10

for topic_idx, topic in enumerate(H):
    print(f"Topic #{topic_idx}")
    print(
        " ".join([feature_names[i] for i in topic.argsort()[: -n_top_words - 1 : -1]])
    )

tf_vectorizer = CountVectorizer(stop_words="english")
tf = tf_vectorizer.fit_transform(documents)
tf_feature_names = tf_vectorizer.get_feature_names()

lda = LatentDirichletAllocation(n_components=n_topics).fit(tf)
lda.fit_transform(tf)
for topic_idx, topic in enumerate(lda.components_):
    print(f"Topic #{topic_idx}")
    print(
        " ".join([feature_names[i] for i in topic.argsort()[: -n_top_words - 1 : -1]])
    )

documents = [
    "This is the first document.",
    "This document is the second document.",
    "And this is the third one",
    "Is this the first document?",
]

tok = Tokenizer()
tok.fit_on_texts(documents)
mat_texts = tok.texts_to_matrix(documents, mode="tfidf")
print(mat_texts)
X = tok.texts_to_sequences(documents)

padded = sequence.pad_sequences(X)
print(X)
print(padded)
