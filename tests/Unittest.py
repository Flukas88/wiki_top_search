# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
import unittest
from wiki_search import get_data


class TopWordsTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_valid_id(self):
        self.assertIsNotNone(get_data('21721040', 5))

    def test_valid_id_ita(self):
        self.assertIsNotNone(get_data('21724', 5, 'it'))

    def test_invalid_id(self):
        self.assertIsNone(get_data('2172104', 5))

    def test_invalid_id_ita(self):
        self.assertIsNone(get_data('21721040', 5, 'it'))


if __name__ == '__main__':
    unittest.main()
