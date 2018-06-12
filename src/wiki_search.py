"""
 Get the top n keywords from wikipedia
"""
# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
# pylint: disable=too-many-locals
# pylint: disable=import-error
# pylint: disable=bad-builtin

from __future__ import division, absolute_import, print_function, unicode_literals
import json
import requests


def clean_word(word):
    """Cleans word from chars that are not allowed

    Arguments:
        word {string} -- the word to be cleaned
    """
    return word.replace('\n', '').replace('=', '').replace('(', '').replace(')', '') \
               .replace('"', '') .replace(',', '').replace('.', '')


def get_data(page_id, top_n, lang='en'):
    """Get data from Wikipedia

    Arguments:
        id {string} -- the id of the page
        top_n {int} -- the top n elements
    """

    data = requests.get(
        'https://{}.wikipedia.org/w/api.php?action=query&prop=extracts&\
        pageids={}&explaintext&format=json'.format(lang, page_id))
    result = json.loads(data.text)
    try:
        info = result['query']['pages'][page_id]['extract']
        #title = result['query']['pages'][page_id]['title']
    except (KeyError, TypeError):
        return None

    tmp_words = [clean_word(el) for el in info.split(' ')]
    words = filter(None, tmp_words)  # remove empty strings
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

    for key, value in words_dict.items():
        inv_map[value] = inv_map.get(value, [])
        inv_map[value].append(key)

    el_words = list(inv_map.values())
    el_count = list(inv_map.keys())
    cnt_list = sorted(el_count[0:top_n], reverse=True)
    ret_word_dict = {}
    for cnt in range(0, len(cnt_list)):
        words_string = ", ".join(el_words[cnt])
        ret_word_dict[cnt_list[cnt]] = words_string
    return ret_word_dict


if __name__ == "__main__":
    print("Finds the top N words by count on Wikipedia\n")
