import re
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from collections import Counter
from nltk.util import ngrams

# Download sekali
# nltk.download('stopwords')

stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()


def clean_text(text: str) -> str:
    if not isinstance(text, str):
        return ""
    

    text = re.sub(r'(https?://\S+|www\.\S+|\S+\.com\S*)', ' ', text)
    text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
    text = re.sub(f"[{re.escape(string.punctuation)}]", " ", text)
    text = re.sub(r'\d+', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()

    tokens = text.split()
    tokens = [t for t in tokens if (t not in stop_words or t in ["not", "no"])]
    tokens = [stemmer.stem(t) for t in tokens]

    return " ".join(tokens)



def apply_text_cleaning(df, col: str, new_col: str = None):
    
    if new_col is None:
        new_col = col

    df[new_col] = df[col].astype(str).apply(clean_text)
    return df


def get_top_words(series, n=20):
    text = " ".join(series)
    freq = nltk.FreqDist(text.split())
    return freq.most_common(n)

def get_top_ngrams(text_series, n=2, top=20):
    
    tokens_list = [t.split() for t in text_series.dropna()]
    
    all_ngrams = []
    for tokens in tokens_list:
        all_ngrams.extend(ngrams(tokens, n))
        
    counter = Counter(all_ngrams)
    return counter.most_common(top)