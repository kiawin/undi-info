undi-info
=========

Scraped listing of Malaysian Electoral Districts from Undi.info



# Dependencies

* Python
* lxml
* mechanize

# How do I use it?

Retrieve Parliment and State Electoral Districts

````bash
$ ./undi-info.py > list.txt
````

Retrieve Parliment Election Results

CSV: parliament-code,election-year,name,party,votes

````bash
$ ./undi-info-results-parliment.py > parliment.csv
````

Retrieve State Election Results

CSV: parliament-code,state-code,election-year,name,party,votes

````bash
$ ./undi-info-results-state.py > state.csv
