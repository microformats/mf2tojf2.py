'''unit tests for mf2tojf2.py '''

import mf2tojf2
import unittest

class BasicCheck(unittest.TestCase):
    def test_checkEmpty(self):
        self.assertEqual(mf2tojf2.mf2tojf2({}), {})
    def test_checkEmptyItems(self):
        self.assertEqual(mf2tojf2.mf2tojf2({"items":[]}), {})
    def test_checkEmptyHentry(self):
         self.assertEqual(mf2tojf2.mf2tojf2({"items":[{"type":["h-entry"]}]}), {'type':'entry'})
    def test_checkFlatHentry(self):
         self.assertEqual(mf2tojf2.mf2tojf2({"items":[{"type": ["h-entry"], "properties": {"url": ["http://kevinmarks.com/hwc2015-06-17.html"], "name": ["Homebrew Website Club notes 2015-06-17"], "published": ["2015-06-17"]}}]}), 
            {
            "type": "entry",
            "published": "2015-06-17",
            "name": "Homebrew Website Club notes 2015-06-17",
            "url": "http://kevinmarks.com/hwc2015-06-17.html"
            })

if __name__ == '__main__':
    unittest.main()
