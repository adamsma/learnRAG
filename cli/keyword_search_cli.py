#!/usr/bin/env python3

import argparse
import json
import string


def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using BM25")
    search_parser.add_argument("query", type=str, help="Search query")

    args = parser.parse_args()

    with open("data/movies.json") as file:
        data = json.load(file)

    rmTbl = str.maketrans("", "", string.punctuation)

    match args.command:
        case "search":
            print(f"Searching for: {args.query}")
            i = 1

            for movie in data["movies"]:

                title = movie["title"].lower().translate(rmTbl)
                query = args.query.lower().translate(rmTbl)

                if query in title:
                    print(f"{i}. {movie["title"]}")
                    i += 1
                
                if i > 5:
                    break

        case _:
            parser.print_help()


if __name__ == "__main__":
    main()