# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
from __future__ import division, absolute_import, print_function, unicode_literals
import json
import sys
import six
import requests


def _cleanWord(word):
    """
    (Internal function) Clean the input from those  chars (=, (, ), " , ', ",", \\n', .) 
    Args: the word to be cleaned
    Return: the cleaned word
    """
    return  word.replace('\n', '').replace('=', '').replace('(', '').replace(')', '').replace('"', '').replace(',', '').replace('.', '')

def getData(id, n):
    """
    Get data \n
    Args: 
    - the *id* of the wikipedia page \n
    - top *n* words to consider

    Return: \n 
    - *None* if *id* is valid \n 
    - *55* if *id* is not valid
    """
    data = requests.get('https://en.wikipedia.org/w/api.php?action=query&prop=extracts&pageids={}&explaintext&format=json'.format(id))
    result = json.loads(data.text)
    try:
        info = result['query']['pages'][id]['extract']
        title = result['query']['pages'][id]['title']
    except KeyError:
        print("Key {} is invalid\n".format(id))
        sys.exit(55)

    tmp_words = [_cleanWord(el) for el in info.split(' ')]
    words = filter(None, tmp_words) # remove empty strings
    words_dict = {}

    for word in words:
        if len(word) < 4:
            pass
        else:
            if word in words_dict:
                words_dict[word] = words_dict[word] + 1
            else:
                words_dict[word] = 1
    inv_map = {}
    for k, v in six.iteritems(words_dict):
        inv_map[v] = inv_map.get(v, [])
        inv_map[v].append(k)

    print("URL: https://en.wikipedia.org/w/api.php?action=query&prop=extracts&pageids={}&explaintext&format=json\n Title: {}\n".format(id, title))
    print("Top {} words:\n".format(n))
    el_words = list(inv_map.values())
    el_count = list(inv_map.keys())
    cnt_list = sorted(el_count[0:n], reverse=True)
    for cnt in range(0, len(cnt_list)):
        words_string = ", ".join(el_words[cnt])
        print("- {} {} \n".format(cnt_list[cnt], words_string))



if __name__ == "__main__":
    print("Finds the top N words by count on wikipedia\n")