# wiki_top_search [![Build Status](https://travis-ci.org/Flukas88/wiki_top_search.svg?branch=master)](https://travis-ci.org/Flukas88/wiki_top_search) [![codecov](https://codecov.io/gh/Flukas88/wiki_top_search/branch/master/graph/badge.svg)](https://codecov.io/gh/Flukas88/wiki_top_search)

Finds the top N words by count on wikipedia


## Dependency 
    $ pipenv install requests
    $ pipenv install six

### How to run it
    $ pipenv run python main.py -id 21721040 -n 1

### Return codes
- *0* (all is fine)
- *55* (id is not valid)
