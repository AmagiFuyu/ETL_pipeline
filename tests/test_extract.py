import unittest
from utils.extract import extract_data
import pandas as pd

class TestExtract(unittest.TestCase):
    def test_extract_data_not_empty(self):
        df = extract_data()
        self.assertIsInstance(df, pd.DataFrame)
        self.assertGreater(len(df), 0)
        self.assertIn("title", df.columns)
        self.assertIn("rating", df.columns)
        self.assertIn("colors", df.columns)
        self.assertIn("timestamp", df.columns)

if __name__ == "__main__":
    unittest.main()