import string
from nltk.stem import PorterStemmer
from .search_utils import DEFAULT_SEARCH_LIMIT, load_movies, load_stopwords

RM_TABLE = str.maketrans("", "", string.punctuation)

def search_command(query, limit = DEFAULT_SEARCH_LIMIT):
    
    results = []
    queryTks = tokenize_text(query)     
            
    for movie in load_movies():

        titleTks = tokenize_text(movie["title"])
        
        if has_matching_token(queryTks, titleTks):
             results.append(movie)
        
        if len(results) >= limit:
            break

    return results

def has_matching_token(queryTokens, titleTokens):
    for qt in queryTokens:
            for tT in titleTokens:
                 if qt in tT:
                      return True
    
    return False

def preprocess_text(text):
    return text.lower().translate(RM_TABLE)

def tokenize_text(text):
    text = preprocess_text(text)
    tokens = text.split()

    for wd in load_stopwords():
        if wd in tokens:
            tokens.remove(wd)

    stemmer = PorterStemmer()

    return [stemmer.stem(x) for x in tokens if x]