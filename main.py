# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
import argparse
import wiki_search

parser = argparse.ArgumentParser(description='Data getting from wikipedia')

parser.add_argument('-id', '--id', required=True)
parser.add_argument('-n', '--n', required=True, type=int)

results = parser.parse_args()

wiki_search.getData(results.id, results.n)
