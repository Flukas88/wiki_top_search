# wiki_top_search [![Build Status](https://travis-ci.org/Flukas88/wiki_top_search.svg?branch=master)](https://travis-ci.org/Flukas88/wiki_top_search) [![codecov](https://codecov.io/gh/Flukas88/wiki_top_search/branch/master/graph/badge.svg)](https://codecov.io/gh/Flukas88/wiki_top_search)

Finds the top N words by count on wikipedia

### How to test it
    $ docker build -t wiki_app .
    $ docker run -d -p 1234:1234 wiki_app
  
Then with a browser open http://127.0.0.1:1234/v1/getinfo/en/21721040/5/

### How to customize it

You can add the CSS style in *static/* and change in the Dockerfile

    COPY ./static/style_cobalt.css $APP_DIR/static/style.css 

### Docker hub

You can pull the Docker image from the hub

    $ docker pull cisco1988/wikipedia_app
