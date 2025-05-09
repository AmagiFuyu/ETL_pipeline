import unittest
import pandas as pd
import os
from utils.load import save_to_csv

class TestLoad(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            "title": ["Hoodie"],
            "price": [320000],
            "rating": [4.5],
            "colors": [2],
            "size": ["L"],
            "gender": ["Men"],
            "timestamp": ["2025-05-09T12:00:00"]
        })

    def test_save_to_csv(self):
        filename = "test_output.csv"
        save_to_csv(self.df, filename)
        self.assertTrue(os.path.exists(filename))
        os.remove(filename)

if __name__ == "__main__":
    unittest.main()