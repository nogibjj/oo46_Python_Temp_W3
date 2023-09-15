from scripts import mpg_cat, my_stats, read_csv
import unittest
import pandas as pd
from pandas.testing import assert_frame_equal

#df = pd.read_csv("../dsets/automobiles.csv")
#
df = read_csv()

class TestMain(unittest.TestCase):
    # def test_return_backwards_string(self):
    #     random_string = "This is my test string"
    #     random_string_reversed = "gnirts tset ym si sihT"
    #     self.assertEqual(random_string_reversed, return_backwards_string(random_string))
     
    def test_col_exist(self):
        test_col_df = df
        test_col_df['Fuel Efficiency'] = test_col_df.loc[:,'mpg'].apply(mpg_cat)
        
        col_name = "Fuel Efficiency"
        message = col_name + " column does not exist"
        # assert if the newly added column exist
        self.assertIn(col_name, test_col_df.columns, message)
        

    def test_my_stats(self):
        test_stats_df = df
        assert_frame_equal(test_stats_df.describe(), my_stats(df)) 


if __name__ == "__main__":
    unittest.main()