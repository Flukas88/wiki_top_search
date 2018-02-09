# wiki_top_search
Finds the top N words by count on wikipedia Edit


## Dependency 
    $ pipenv install requests
    $ pipenv install six

### How to run it
    $ pipenv run python main.py -id 21721040 -n 1

### Return codes
- *0* (all is fine)
- *55* (id is not valid)
