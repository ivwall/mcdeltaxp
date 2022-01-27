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

    def test01_pull_coinstats_and_store(self):
        MCDelta.writejson_to_timestamp_file()

    def test12_generate_from_scratch_mcdelta_11json_file(self):
        MCDelta.generate_from_scratch_mcdelta_11json_file()

    #def test13_update_mcdelta_11json_file(self):
    #    MCDelta.update_mcdelta_11json_file()

    def test15_market_cap_delta_display(self):
        MCDelta.market_cap_delta_scan_and_display_markups()

    def test16_market_cap_delta_display_from_04json_to_dev4_html(self):
        MCDelta.write_mcdelta_html_from_04json_data()
    
    def test17_write_mcdelta_html_from_11json_data(self):
        MCDelta.write_mcdelta_html_from_11json_data()

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