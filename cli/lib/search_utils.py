import json
import os

DEFAULT_SEARCH_LIMIT = 5

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DATA_PATH = os.path.join(PROJECT_ROOT, "data", "movies.json")
STOPWORDS_PATH = os.path.join(PROJECT_ROOT, "data", "stopwords.txt")

def load_movies():
    with open(DATA_PATH) as file:
        data = json.load(file)

    return data["movies"]

def load_stopwords():
    with open(STOPWORDS_PATH) as file:
        stopwords = file.read().splitlines()
    
    return stopwords