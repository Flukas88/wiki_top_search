# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
import unittest
import wiki_search


class TopWordsTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_valid_id(self):
        wiki_search.getData('21721040', 5)
        
    def test_invalid_id(self):
        with self.assertRaises(SystemExit) as cm:
            wiki_search.getData('2172104', 5)

        self.assertEqual(cm.exception.code, 55)

if __name__ == '__main__':
    unittest.main()
