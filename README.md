# wiki_top_search [![Build Status](https://travis-ci.org/Flukas88/wiki_top_search.svg?branch=master)](https://travis-ci.org/Flukas88/wiki_top_search) [![codecov](https://codecov.io/gh/Flukas88/wiki_top_search/branch/master/graph/badge.svg)](https://codecov.io/gh/Flukas88/wiki_top_search)

Finds the top N words by count on wikipedia

### How to test it
    $ docker build -t wiki_app .
    $ nohup docker run -p 5000:5000 wiki_app &
  
Then with a browser open http://127.0.0.1:5000/v1/getinfo/en/21721040/5/

### How to customize it

You can change the CSS style in *static/style.css*
