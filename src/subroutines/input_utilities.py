"""

"""
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
