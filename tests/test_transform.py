import unittest
import pandas as pd
from utils.transform import transform_data

class TestTransform(unittest.TestCase):
    def test_transform_cleans_data_properly(self):
        dummy = pd.DataFrame({
            "title": ["Unknown Product", "T-shirt"],
            "price": ["$100.00", "$50.00"],
            "rating": ["⭐ 4.8 / 5", "⭐ 3.5 / 5"],
            "colors": ["3 Colors", "2 Colors"],
            "size": ["Size: L", "Size: M"],
            "gender": ["Gender: Men", "Gender: Women"],
            "timestamp": ["2025-05-09T12:00:00", "2025-05-09T12:00:00"]
        })

        result = transform_data(dummy)
        self.assertEqual(len(result), 1)  # Unknown Product dihapus
        self.assertEqual(result.iloc[0]["price"], 800000)  # $50 * 16,000
        self.assertIsInstance(result.iloc[0]["rating"], float)
        self.assertEqual(result.iloc[0]["colors"], 2)
        self.assertEqual(result.iloc[0]["size"], "M")
        self.assertEqual(result.iloc[0]["gender"], "Women")

if __name__ == "__main__":
    unittest.main()