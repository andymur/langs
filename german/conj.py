#!/usr/bin/python3

from bs4 import BeautifulSoup
from urllib.request import urlopen
import sys

pronouns = ('ich', 'du', 'er_sie_es', 'wir', 'ihr', 'sie')

def conjugator_reverso_source(pronouns, verb):
	url = 'http://conjugator.reverso.net/conjugation-german-verb-' + verb + '.html'
	document = urlopen(url)
	print("downloading...." + url)
	content = document.read()
	soup = BeautifulSoup(content, 'html.parser')
	divs = soup.find_all('div', {'class': 'wrap-three-col'})
	present_tense = divs[4]

	present_verbs = []

	for item in present_tense.find_all('li'):
		present_verbs.append(item.find('i', {'class': 'verbtxt'}).get_text() + item.find('i', {'class': 'verbtxt-term'}).get_text())

	return zip(pronouns, tuple(present_verbs))

def wiktionary_get_verb_from_table_row(table_row):
	return table_row.find_all('td')[1].get_text().strip()

def wiktionary_source(pronouns, verb):
	url = "https://de.wiktionary.org/wiki/" + verb
	document = urlopen(url)
	print("downloading...." + url)
	content = document.read()
	soup = BeautifulSoup(content, 'html.parser')

	inflection_table = soup.find('table', {'class': 'wikitable'})
	
	if inflection_table:
		present_verbs = []
		present_rows = inflection_table.find_all('tr')[1:4]
		past_row = inflection_table.find_all('tr')[4]
		
		first_singular, second_singular, third_singular = present_rows
		
		first_singular_verb = wiktionary_get_verb_from_table_row(first_singular)
		second_singular_verb = wiktionary_get_verb_from_table_row(second_singular)
		third_singular_verb = wiktionary_get_verb_from_table_row(third_singular)

		first_past_singular_verb = wiktionary_get_verb_from_table_row(past_row)
		#print(first_past_singular_verb)

		#return zip(pronouns, [first_singular_verb, second_singular_verb, third_singular_verb, verb, verb, verb])
		return zip(pronouns, [first_past_singular_verb, first_past_singular_verb + "st", first_past_singular_verb, 
			first_past_singular_verb + "en", first_past_singular_verb + "t", first_past_singular_verb + "en"])

	return zip(pronouns, pronouns)

if __name__ == "__main__":

	arguments = sys.argv[1:]

	if len(arguments) == 1:
		verb = arguments[0]
		source = "conjugator"
	else:
		source = arguments[0]
		verb = arguments[1]

	print("trying to conjugate verb " + verb + " from source " + source)

	if source == "wiki":
		result = wiktionary_source(pronouns, verb)
	elif source == "conjugator":
		result = conjugator_reverso_source(pronouns, verb)
	else:
		result = None

	print("here is result coming...", list(result) if result else None)