import unittest
import subprocess

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

    def test11_zip_n_deploy(self):
        print("")
        subprocess.run(["ls", "-l"])
        print("")
        subprocess.run(["sudo", "su -"])
        print("")
        print(os.getcwd())
        print("")
        os.chdir('/home/dlt03/gitprojects/mcdeltaxp/mcdeltaxp')
        print("")
        print(os.getcwd())
        print("")
        subprocess.run(["ls", "-l"])
        print("")
        subprocess.run(["jar", "cvf", "mcdelta.war", "mcdelta"])
        print("")
        subprocess.run(["ls", "-l"])
        print("")
        print("")
        subprocess.run(["sudo", "rm", "/opt/tomcat/latest/webapps/mcdelta.war"])
        print("")
        subprocess.run(["sudo", "cp", "mcdelta.war", "/opt/tomcat/latest/webapps/"])
        print("")
        subprocess.run(["ls", "-l"])
        print("")
        subprocess.run(["rm", "mcdelta.war"])
        print("")
        subprocess.run(["ls", "-l"])
        print("")
        print("      zip n deploy ")

    def test12_start_processing_data(self):
        MCDelta.process_data_number01()

    def test13_develop_mcdelta_json(self):
        MCDelta.develop_mcdelta_json()

    def test14_start_writing_html_file(self):
        MCDelta.write_html_file()

    def test15_read_update_write_json(self):
        MCDelta.ruwb_json()

    def test16_write_mcdelta_html_from_json_data(self):
        MCDelta.write_mcdelta_html_from_json_data()

if __name__ == '__main__':
    unittest.main()