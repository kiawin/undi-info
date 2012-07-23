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

#Parliament Constituency Listings
parliament_places = []
parliament_codes = []

for state in state_slugs:
	path = "div#parl_listing div.content ul li.negeri_p_"+state+"_li a"
	links = html.cssselect(path)
	for link in links:
		parliament_places.append(link.cssselect("span.place")[0].text)
		parliament_codes.append(link.cssselect("span.code")[0].text)

#State Constituency Listings
state_places = []
state_codes = []

for state in state_slugs:
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
print "Parliament Constituency Listings"
total_parliament_places = len(parliament_places)
for i in range(total_parliament_places):
	print parliament_codes[i]+": "+parliament_places[i]


print ""
print "State Constituency Listings"
total_state_places = len(state_places)
for i in range(total_state_places):
	print state_codes[i]+": "+state_places[i]
