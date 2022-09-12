import argparse
from typing import List
import json
from csv import reader


def read_book_list(filename: str) -> List[dict]:
    with open(filename, "r") as f:
        books = json.load(f)
    return books


def read_key_list(filename: str) -> dict:
    lookup_table = {}
    with open(filename, 'r') as f:
        rows = reader(f)
        # skip the header
        next(rows)
        # iterate through the rows
        for row in rows:
            # store as variables for readability
            genre = row[0].strip()
            keywords_and_points = (row[1].strip(), int(row[2].strip()))
            if genre not in lookup_table:
                # add the key
                lookup_table[genre] = [keywords_and_points]
            else:
                lookup_table[genre].append(keywords_and_points)
        return lookup_table

def evaluate_genre(description, keyword_list):
    phrases_seen = set()
    point_scores = 0
    total_occurances = 0
    for keyword_tuple in keyword_list:
        keyword = keyword_tuple[0]
        points = keyword_tuple[1]
        keyword_occurances = description.count(keyword)
        if keyword_occurances > 0:
            # we also need to check if its unique or not, and then add points based on that
            if keyword not in phrases_seen:
                phrases_seen.add(keyword)
                point_scores += points
            total_occurances += keyword_occurances
    # calculate average point score (k) of all occurances
    # look for a short circuit if either point scores or phrases len is 0
    if point_scores == 0 or len(phrases_seen) == 0:
        return 0
    k = point_scores / len(phrases_seen)
    # return the genre score (n * k)
    return total_occurances * k


def score(description, lookup_table):
    # set description to lowercase to avoid issues with matching
    description = description.lower()
    # make a table of scores and genres
    table = {}
    # go through each genre in the lookup table first
    for genre in lookup_table.keys():
        table[genre] = evaluate_genre(description, lookup_table[genre])
    return table

parser = argparse.ArgumentParser()
parser.add_argument('book_list')
parser.add_argument('keyword_file')
args = parser.parse_args()

book_list = args.book_list
keyword_file = args.keyword_file

books = read_book_list(book_list)
keywords = read_key_list(keyword_file)

for book in books:
    print(book["title"])
    table = score(book["description"], keywords)
    for genre in table.keys():
        if table[genre] != 0:
            print(f"{genre}, {int(table[genre])}")
    print()
