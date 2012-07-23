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

````bash
$ ./undi-info-results-parliment.py > parliment.txt
````

Retrieve State Election Results

````bash
$ ./undi-info-results-state.py > state.txt
