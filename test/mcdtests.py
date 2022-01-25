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

    def test06_writejson_to_timestamp_file_v1_datetime_str(self):
        MCDelta.writejson_to_timestamp_file_v1_datetime_str()

    def test07_writejson_to_new_filename(self):
        MCDelta.writejson_to_new_filename()

    def test08_writejson_to_timestamp_file(self):
        MCDelta.writejson_to_timestamp_file()

    def test09_list_data_files(self):
        MCDelta.list_data_files()

    def test10_read_last_data_file(self):
        MCDelta.read_last_data_file()

    def test11_generate_from_scratch_mcdelta_11json_file(self):
        MCDelta.generate_from_scratch_mcdelta_11json_file()

    def test12_update_mcdelta_11json_file(self):
        MCDelta.update_mcdelta_11json_file()
    
    def test15_read_update_write_json(self):
        MCDelta.ruwb_json()

    def test16_write_mcdelta_html_from_03json_data(self):
        MCDelta.write_mcdelta_html_from_03json_data()

    def test17_write_mcdelta_html_from_04json_data(self):
        MCDelta.write_mcdelta_html_from_04json_data()

    def test19_update_mcdelta_0x_from_raw_data(self):
        MCDelta.update_mcdelta_0x_from_raw_data()

    def test30_zip_n_deploy(self):
        #print("")
        subprocess.run(["ls", "-l"])
        #print("")
        subprocess.run(["sudo", "su -"])
        #print("")
        #print(os.getcwd())
        #print("")
        os.chdir('/home/dlt03/gitprojects/mcdeltaxp/mcdeltaxp')
        #print("")
        #print(os.getcwd())
        #print("")
        subprocess.run(["ls", "-l"])
        #print("")
        subprocess.run(["jar", "cvf", "mcdelta.war", "mcdelta"])
        #print("")
        subprocess.run(["ls", "-l"])
        #print("")
        #print("")
        subprocess.run(["sudo", "rm", "/opt/tomcat/latest/webapps/mcdelta.war"])
        #print("")
        subprocess.run(["sudo", "cp", "mcdelta.war", "/opt/tomcat/latest/webapps/"])
        #print("")
        #subprocess.run(["ls", "-l"])
        print("")
        subprocess.run(["rm", "mcdelta.war"])
        #print("")
        subprocess.run(["ls", "-l"])
        #print("")
        print("      zip n deploy ")

if __name__ == '__main__':
    unittest.main()