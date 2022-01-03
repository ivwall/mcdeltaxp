import unittest

# ------------------------------------------------
# https://stackoverflow.com/questions/54598292/python-modulenotfounderror-when-trying-to-import-module-from-imported-package/54613085
import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from pathlib import Path
path = Path(myDir)
a=str(path.parent.absolute())

sys.path.append(a)
# ------------------------------------------------

from mcdeltaxp.mark_cap_delta import MCDelta

class TDDmcdelta(unittest.TestCase):
    def setUp(self):
        a = "b"

    def test01(self):
        print("mcdelta test01")

    def test02(self):
        pass

    def test03(self):
        MCDelta.wud()

    def test04_pull_data(self):
        MCDelta.get_coin_stats()

    def test05_walk_the_tree_pull_coin_n_cap(self):
        MCDelta.pull_coin_n_market_cap()

    def test06_timestamp(self):
        MCDelta.displaytimestamp()

    def test07_create_file_with_timestamp_name(self):
        MCDelta.create_file_with_timestamp_name()

    def test08_writejson_to_timestamp_file(self):
        MCDelta.writejson_to_timestamp_file()

    def test09_list_data_files(self):
        MCDelta.list_data_files()

    def test10_read_last_data_file(self):
        MCDelta.read_last_data_file()

if __name__ == '__main__':
    unittest.main()