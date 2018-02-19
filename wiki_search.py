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
    - end_string: the string containing the info requested or an invalid key message
    """
    end_string = ''
    data = requests.get('https://en.wikipedia.org/w/v1.php?action=query&prop=extracts&pageids={}&explaintext&format=json'.format(id))
    result = json.loads(data.text)
    try:
        info = result['query']['pages'][id]['extract']
        title = result['query']['pages'][id]['title']
    except (KeyError, TypeError):
        end_string += "Key <b>{}</b> is invalid </br>".format(id)
        return end_string

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

    end_string += "<b>URL:</b> <i>https://en.wikipedia.org/w/v1.php?action=query&prop=extracts&pageids={}&explaintext&format=json</i></br> <b>Title</b>: {}</br>".format(id, title)
    end_string += "<b>Top <i>{}</i> words</b>:</br>".format(n)
    el_words = list(inv_map.values())
    el_count = list(inv_map.keys())
    cnt_list = sorted(el_count[0:n], reverse=True)
    end_string += '<table style="width:70%; border: 2px solid black"><tr><th>Count</th><th>Words</th></tr>'
    for cnt in range(0, len(cnt_list)):
        words_string = ", ".join(el_words[cnt])

        end_string += "<tr><td>{}</td><td>{}</td></tr>".format(cnt_list[cnt], words_string)
    end_string += '</table>'
    return end_string



if __name__ == "__main__":
    print("Finds the top N words by count on wikipedia\n")
