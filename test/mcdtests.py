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

    def test01_get_raw_coinstats_on_run(self):
        MCDelta.get_raw_coinstats_on_run()

    def test13_update_mcdelta_11json_file(self):
        MCDelta.update_mcdelta_11json_file()

    def test15_market_cap_delta_display(self):
        MCDelta.market_cap_delta_scan_and_display_markups()

    def test17_write_mcdelta_html_from_11json_data(self):
        MCDelta.write_mcdelta_html_from_11json_data()

    #--------------------------------------------------------------------------
    # KEEP THIS
    #def test29_file_dates(self):
    #    MCDelta.list_file_dates()
    def test30_zip_n_deploy(self):
        subprocess.run(["ls", "-l"])
        subprocess.run(["sudo", "su -"])
        #gotoDir = '/home/dlt06/git-work/git-mcdelta/mcdeltaxp/mcdeltaxp' 
        gotoDir = '/home/dlt01/git/mcdeltaxp/mcdeltaxp' 
        os.chdir(gotoDir)
        subprocess.run(["ls", "-l"])
        subprocess.run(["jar", "cvf", "mcdelta.war", "mcdelta"])
        subprocess.run(["ls", "-l"])
        subprocess.run(["sudo", "rm", "/opt/tomcat/webapps/mcdelta.war"])
        subprocess.run(["sudo", "cp", "mcdelta.war", "/opt/tomcat/webapps/"])
        print("")
        subprocess.run(["rm", "mcdelta.war"])
        subprocess.run(["ls", "-l"])
        print("      zip n deploy ")

if __name__ == '__main__':
    unittest.main()