import unittest
from src.subroutines.input_utilities import *

SAMPLE_BOOK_LIST_ONE = "./tests/sample_book_list_one.json"
SAMPLE_BOOK_LIST_TWO = "./tests/sample_book_list_two.json"
SAMPLE_KEYPHRASE_LIST_ONE = "./tests/keyphrase_list_one.csv"


class TestInputFunctions(unittest.TestCase):
    def test_read_book_list_one(self) -> None:
        book_list = read_book_list(SAMPLE_BOOK_LIST_ONE)
        expected_book_list = [
            {
                "title": "Harry Potter",
                "description": "The story of a hat with a grudge that makes a school full of children's lives "
                               "miserable.  Will the lovable groundskeeper be able to keep the school open?  Find "
                               "out!",
            }
        ]
        # check if the two lists have the same elements
        self.assertListEqual(book_list, expected_book_list)

    def test_read_book_list_two(self):
        book_list = read_book_list(SAMPLE_BOOK_LIST_TWO)
        expected_book_list = [
            {
                "title": "The Cat in the Hat",
                "description": "This bestselling thriller has captivated millions, and teaches the importance of "
                               "listening to fish.",
            },
            {
                "title": "The Hunger Games",
                "description": "A charming cookbook that helps make beating hunger fun!",
            },
        ]
        self.assertListEqual(book_list, expected_book_list, "Read Error; Mismatch.")

    def test_read_key_list(self):
        keyphrase_dict = read_key_list(SAMPLE_KEYPHRASE_LIST_ONE)
        expected_keyphrase_dict = {
            "action": [("katana", 6), ("sweet motorcycle", 4)],
            "biography": [("mists of time", 2), ("born and raised", 3)],
            "how to": [("sweet motorcycle", 6)]
        }
        self.assertDictEqual(keyphrase_dict, expected_keyphrase_dict)


if __name__ == "__main__":
    unittest.main()
