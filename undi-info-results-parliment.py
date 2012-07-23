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

for state in state_slugs:
	path = "div#parl_listing div.content ul li.negeri_p_"+state+"_li a"
	links = html.cssselect(path)
	for link in links:
		parliment_places.append(link.cssselect("span.place")[0].text)
		parliment_codes.append(link.cssselect("span.code")[0].text)

url = 'http://undi.info/ajax.php?a=info&c='

for parliment_code in parliment_codes:
	url_ajax = url+parliment_code
	req = mechanize.Request(url_ajax)
	resp = mechanize.urlopen(req)
	html = lxml.html.parse(resp).getroot()
	#years = html.cssselect("div.info_body div.year")
	
	for year_code in ['2008','2004']:
		path = "div.year_"+year_code+" div.party_list"
		party_lists = html.cssselect(path)
		
		for party_list in party_lists:
			votes = party_list.cssselect("div.votes")[0].text
			party_name = party_list.cssselect("div.party_name")[0].text
			candidate_name = party_list.cssselect("div.cand_name")[0].text
			votes = votes.replace(',','')
			print parliment_code+','+year_code+','+candidate_name+','+party_name+','+votes
	print ''

#Temporary output
