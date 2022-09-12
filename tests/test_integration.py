import unittest
from src.subroutines import input_utilities
from src.subroutines import classification_algorithm

PROVIDED_BOOK_LIST = "./tests/data/provided_book_data.json"
PROVIDED_KEYWORD_LIST = "./tests/data/provided_keyword_file.csv"


class IntegrationTest(unittest.TestCase):
    def test_integration(self) -> None:
        books = input_utilities.read_book_list(PROVIDED_BOOK_LIST)
        keywords = input_utilities.read_key_list(PROVIDED_KEYWORD_LIST)
        scores = []
        for book in books:
            scores.append(classification_algorithm.score(book["description"], keywords))
        # check infinite jest
        self.assertIn("literary fiction", scores[0].keys())
        self.assertIn("action", scores[1].keys())
        self.assertIn("sci-fi", scores[1].keys())
        self.assertEqual(scores[0]["literary fiction"], 12)
        self.assertEqual(scores[1]["sci-fi"], 8)
        self.assertEqual(scores[1]["action"], 15)


if __name__ == "__main__":
    unittest.main()
