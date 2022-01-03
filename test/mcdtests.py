import unittest

import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from pathlib import Path
path = Path(myDir)
a=str(path.parent.absolute())

sys.path.append(a)


from mcdeltaxp.mark_cap_delta import MCDelta

class TDDmcdelta(unittest.TestCase):
    def setUp(self):
        a = "b"

    def test01(slef):
        print("mcdelta test01")

    def test02(self):
        pass

    def test03(slef):
        MCDelta.wud()

if __name__ == '__main__':
    unittest.main()