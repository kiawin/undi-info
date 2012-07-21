#!/usr/bin/env python

import mechanize
import lxml.html

url = 'http://undi.info'

req = mechanize.Request(url)
resp = mechanize.urlopen(req)
html = lxml.html.parse(resp).getroot()

#State Listings
links = html.cssselect("div.negeri_nav ul li a")

state_names = []
state_slugs = []
state_plates = []

for link in links:
	state_names.append(link.text.lower())
	state_slugs.append(link.attrib.get('slug'))
	state_plates.append(link.attrib.get('plate'))

#Parliment Constituency Listings
parliment_places = []
parliment_codes = []

for state in state_names:
	path = "div#parl_listing div.content ul li.negeri_p_"+state+"_li a"
	links = html.cssselect(path)
	for link in links:
		parliment_places.append(link.cssselect("span.place")[0].text)
		parliment_codes.append(link.cssselect("span.code")[0].text)

#State Constituency Listings
state_places = []
state_codes = []

for state in state_names:
	path = "div#state_listing div.content ul li.negeri_n_"+state+"_li a"
	links = html.cssselect(path)
	for link in links:
		state_places.append(link.cssselect("span.place")[0].text)
		state_codes.append(link.cssselect("span.code")[0].text)
		
		
		
#Temporary output
print "States"
total_states = len(state_names)
for i in range(total_states):
	print state_plates[i]+": "+state_names[i]


print ""	
print "Parliment Constituency Listings"
total_parliment_places = len(parliment_places)
for i in range(total_parliment_places):
	print parliment_codes[i]+": "+parliment_places[i]


print ""
print "State Constituency Listings"
total_state_places = len(state_places)
for i in range(total_state_places):
	print state_codes[i]+": "+state_places[i]
