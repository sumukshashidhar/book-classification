"""
Main Driver file for the classification

Author: Sumuk Shashidhar (sumuks2@illinois.edu)
Date Revised: Monday 12th September 2022
"""
# for argument parsing
import argparse

from subroutines import classification_algorithm

# internal modules
from subroutines import input_utilities

parser = argparse.ArgumentParser(
    description="Classify books into different genres based on description keywords"
)
# add the necessary arguments
parser.add_argument(
    "book_list",
    metavar="B",
    help="Absolute / Relative Path to the JSON book list",
    type=str,
)
parser.add_argument(
    "keyword_file",
    metavar="K",
    help="Absolute / Relative Path to a file containing keywords",
    type=str,
)

# parse them, assign them to variables
args = parser.parse_args()
book_list = args.book_list
keyword_file = args.keyword_file

# try to read the given files
books = input_utilities.read_book_list(book_list)
keywords = input_utilities.read_key_list(keyword_file)

# for each book, print out the title, and the classification scores for each genre, as long as it is not 0
for book in books:
    print(book["title"])
    table = classification_algorithm.score(book["description"], keywords)
    for genre in table.keys():
        if table[genre] != 0:
            print(f"{genre}, {table[genre]}")
    print()
