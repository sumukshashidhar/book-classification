"""
Functions to handle the input files (list of books, list of keywords)

Author: Sumuk Shashidhar (sumuks2@illinois.edu)
Date Revised: Monday 12th September 2022
"""

# to load the JSON file into python
import json

# to read CSV files
from csv import reader

# the typing module, for specifying function arguments and return types
from typing import List, Dict, Tuple


def read_book_list(filename: str) -> List[dict]:
    """
    Reads the list of books from the JSON file
    :param filename: str: The path to the JSON file with the list of books
    :return: Dict: The loaded JSON file
    """
    try:
        with open(filename, "r") as f:
            # load the books into a python dictionary
            books = json.load(f)
        return books
    except FileNotFoundError:
        raise FileNotFoundError(
            "The JSON file containing the books was not found. Please try an absolute path."
        )
    except json.JSONDecodeError:
        raise RuntimeError(
            "The passed JSON file is invalid. Please make sure the file is a valid JSON"
        )


def read_key_list(filename: str) -> Dict[str, List[Tuple[str, int]]]:
    """
    Reads the keyword list based on genres, and stores the points in an interesting data structure
    :param filename:
    :return: Dict[str, List[Tuple[str, int]]]: A dictionary where genres are keys and a list of keywords with scores
                                                are the values
    """
    # create a lookup table
    lookup_table = {}
    try:
        # open up the file
        with open(filename, "r") as f:
            rows = reader(f)
            # skip the header
            next(rows)
            # iterate through the rows
            for row in rows:
                # store as variables for readability
                genre = row[0].strip()
                # make a tuple with keywords and points
                keywords_and_points = (row[1].strip(), int(row[2].strip()))
                if genre not in lookup_table:
                    # add the key
                    lookup_table[genre] = [keywords_and_points]
                else:
                    lookup_table[genre].append(keywords_and_points)
            return lookup_table
    except FileNotFoundError:
        raise FileNotFoundError(
            "The CSV file containing the keywords was not found. Please try an absolute path."
        )
    except RuntimeError:
        raise RuntimeError(
            "The passed CSV file is invalid. Please make sure the file is a valid JSON"
        )
