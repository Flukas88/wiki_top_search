# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
from __future__ import division, absolute_import, print_function, unicode_literals
import json
import six
import requests

def clean_word(word):

    """Cleans word from chars that are not allowed

    Arguments:
        word {string} -- the word to be cleaned
    """
    return word.replace('\n', '').replace('=', '').replace('(', '').replace(')', '') \
               .replace('"', '') .replace(',', '').replace('.', '')


def get_data(page_id, n, lang='en'):

    """Get data from wikipedia

    Arguments:
        id {string} -- the id of the page
        n {int} -- descrithe top n elements
    """

    end_string = ''
    data = requests.get(
        'https://{}.wikipedia.org/w/api.php?action=query&prop=extracts&\
        pageids={}&explaintext&format=json'.format(lang, page_id))
    result = json.loads(data.text)
    try:
        info = result['query']['pages'][page_id]['extract']
        title = result['query']['pages'][page_id]['title']
    except (KeyError, TypeError):
        end_string += "Key <b>{}</b> is invalid </br>".format(page_id)
        return end_string

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
    
    for key, value in enumerate(words_dict.items())
        inv_map[value] = inv_map.get(value, [])
        inv_map[value].append(key)

    end_string += "<b>URL:</b> <i>https://{}.wikipedia.org/w/api.php\
                  ?action=query&prop=extracts&pageids={}&explaintext&\
                  format=json</i></br> <b>Title</b>: {}</br>"\
                  .format(lang, page_id, title)
    end_string += "<b>Top <i>{}</i> words</b>:</br>".format(n)
    el_words = list(inv_map.values())
    el_count = list(inv_map.keys())
    cnt_list = sorted(el_count[0:n], reverse=True)
    end_string += '<table style="width:70%;border: 2px solid black"> \
                  <tr><th>Count</th><th>Words</th></tr>'
    for cnt in range(0, len(cnt_list)):
        words_string = ", ".join(el_words[cnt])
        end_string += "<tr><td>{}</td><td>{}</td></tr>".format(
            cnt_list[cnt], words_string)
    end_string += '</table>'
    return end_string


if __name__ == "__main__":
    print("Finds the top N words by count on wikipedia\n")
