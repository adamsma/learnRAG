#!/usr/bin/env python3

import argparse
import json
import string
from nltk.stem import PorterStemmer

def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using BM25")
    search_parser.add_argument("query", type=str, help="Search query")

    args = parser.parse_args()

    with open("data/movies.json") as file:
        data = json.load(file)

    with open("data/stopwords.txt") as file:
        stopwords = file.read().splitlines()

    rmTbl = str.maketrans("", "", string.punctuation)
    stemmer = PorterStemmer()

    match args.command:
        case "search":
            print(f"Searching for: {args.query}")
            i = 1

            queryTks = [x for x in args.query.lower().translate(rmTbl).split(" ") if x != ""]

            for wd in stopwords:
                if wd in queryTks:
                    queryTks.remove(wd)
            
            for movie in data["movies"]:

                titleTks = [x for x in movie["title"].lower().translate(rmTbl).split(" ") if x != ""]
                for wd in stopwords:
                    if wd in titleTks:
                        titleTks.remove(wd)

                for qt in queryTks:
                    for tT in titleTks:
                        qt = stemmer.stem(qt)
                        tT = stemmer.stem(tT)
                        
                        if qt in tT:
                            print(f"{i}. {movie["title"]}")
                            i += 1
                            break

                    if qt in tT:
                            break
                
                if i > 5:
                    break

        case _:
            parser.print_help()


if __name__ == "__main__":
    main()