import argparse
from subroutines import input_utilities
from subroutines import classification_algorithm

parser = argparse.ArgumentParser()
parser.add_argument('book_list')
parser.add_argument('keyword_file')
args = parser.parse_args()

book_list = args.book_list
keyword_file = args.keyword_file

books = input_utilities.read_book_list(book_list)
keywords = input_utilities.read_key_list(keyword_file)

for book in books:
    print(book["title"])
    table = classification_algorithm.score(book["description"], keywords)
    for genre in table.keys():
        if table[genre] != 0:
            print(f"{genre}, {int(table[genre])}")
    print()
