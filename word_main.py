# 필요한 라이브러리 import
import nltk
import streamlit as st
import glob
import pandas as pd
import src
import matplotlib.pyplot as plt
import torch

#from wordcloud import WordCloud
from collections import Counter
from konlpy.tag import Okt
from konlpy.utils import pprint

st.title('WORD CLOUD 연습')

files = glob.glob('./*.xlsx')

@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

# st.write('선택된 데이터 파일', option)

with st.sidebar:
    uploadeded_file = st.file_uploader('파일 업로드')

    uploadeded_file = st.selectbox(
         '데이터 파일을 선택해 주세요?',
        files
    )

    download_area = st.empty()

if uploadeded_file:
    # 업로드 완료시
    df = pd.read_excel(uploadeded_file)
    # st.dataframe(df)

#
txt = st.text_area(
    "",)

st.write(f'You wrote {len(txt)} characters.')

btn = st.button('선택완료')

# 전처리
okt = Okt()

# 텍스트 토큰화 (Tokenization)

# 텍스트 데이터 불러오기
text = open('D:/SKEC Files/Documents/PPM.txt', 'r', encoding='utf-8').read()

# 전처리
#okt = Okt()
#tokens = okt.nouns(text)
#count = Counter(tokens)

# 전처리
okt = Okt()

# 텍스트 토큰화 (Tokenization)
tokens = okt.morphs(text)

#정제 (Cleaning) 및 정규화 (Normalization)
cleaned_tokens = [token for token in tokens if token.isalnum()]

# 어간 추출 (Stemming)
stemmer = nltk.stem.PorterStemmer()
stemmed_tokens = [stemmer.stem(token) for token in cleaned_tokens]

# 표제어 추출 (Lemmatization)
nltk.download('wordnet')
lemmatizer = nltk.stem.WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(token) for token in cleaned_tokens]


# 불용어 (Stopword) 제거
stop_words = set(["은", "는", "이", "가", "을", "를","및","으로","의","하여","하고","에서","에게","한다","에", "또는", "하는", "경우", 
                  "또한","과","해야","있도록", "통해","하며", "따라","대한","관련","등"])
filtered_tokens = [token for token in cleaned_tokens if token not in stop_words]
count = Counter(filtered_tokens)

# 워드클라우드 생성

wordcloud = WordCloud(font_path='c:/Windows/Fonts/Malgun.ttf', background_color='white')
wordcloud.generate_from_frequencies(count)


# 시각화
plt.figure(figsize=(15,15))
plt.imshow(wordcloud)
plt.axis('on')
plt.show()
