# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
import sys, os
sys.path.append(os.path.abspath('../wiki_top_search/src'))
import unittest
from wiki_search import get_data

class TopWordsTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_valid_id(self):
        self.assertIn("URL", get_data('21721040', 5))
        
    def test_invalid_id(self):
        self.assertIn("invalid", get_data('2172104', 5))

if __name__ == '__main__':
    unittest.main()
