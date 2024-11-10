import numpy as np 
import pandas as pd
import re
import nltk
import os
from django.conf import settings
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity
from django.conf import settings
import time
import joblib

nltk.download("stopwords")
stopwords=stopwords.words('english')

stemmer = SnowballStemmer("english")
analize = CountVectorizer().build_analyzer()

path = os.path.join(settings.BASE_DIR,'static/wines/winedata.xlsx')
df = pd.read_excel(path)
df["text_reviews"] = df['description']



def text_process(text):
    text = re.sub('[^a-z\s]','', text.lower())
    text = [word for word in text.split(" ") if word not in stopwords]
    return " ".join(text)

def stem_text(text):
    return (stemmer.stem(word) for word in analize(text))

df['text_reviews'] = df['text_reviews'].apply(text_process)
count = CountVectorizer(analyzer = stem_text)
count_matrix = count.fit_transform(df['text_reviews'])
tf_idf = TfidfTransformer()
train_tfidf = tf_idf.fit_transform(count_matrix)
joblib.dump(train_tfidf,"train_tfidf.pkl")
#Return top 3 most relative

def search(query):
    
    start = time.time()
    query = text_process(query)
    query_matrix = count.transform([query])
    query_tfidf = tf_idf.transform(query_matrix)
    sim_score = cosine_similarity(query_tfidf,train_tfidf)
    sorted_indexes = np.argsort(sim_score).tolist()
    top_three = sorted_indexes[0][-3:]
    end = time.time()
    print(end-start)
    return df.iloc[top_three][['designation','variety','description','country']]