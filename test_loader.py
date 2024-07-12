import unittest
import json

class Test1(unittest.TestCase):
    movies = []

    @classmethod
    def setUpClass(cls) -> None:
        with open('movies.json') as f:
            cls.movies = json.load(f)
    

    def test_rank(self):
        self.assertEqual(self.movies[0]["Rank"], 1)

    def test_title(self):
        self.assertEqual(self.movies[0]["Title"], "Avatar")

if __name__ == '__main__':
    unittest.main()

    