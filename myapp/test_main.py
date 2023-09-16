from scripts import my_stats, read_csv
import unittest
import polars as pl
from polars.testing import assert_frame_equal

df = read_csv()
my_stat = my_stats(df)


class TestMain(unittest.TestCase):
    def test_count(self):
        my_count = df.select(pl.count()).item()
        message = "Expected: {} but got {}".format(392, my_count)

        # assert if dataframe values count is as expected
        self.assertEqual(my_count, 392, message)

    # Simple usage of polars testing
    def test_my_stats(self):
        assert_frame_equal(my_stat, my_stats(df))


if __name__ == "__main__":
    unittest.main()
