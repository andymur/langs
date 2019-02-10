#!/usr/bin/python3

from bs4 import BeautifulSoup
from urllib.request import urlopen
import sys

cases = ('nominativ', 'genitiv', 'dativ', 'akkusative')
number = ('singular', 'plural')

def wikitionary_case_singular_plural_nouns(case_row):
	tds = case_row.find_all('td')
	return [tds[0].get_text().strip(), tds[1].get_text().strip()]


def wiktionary_source(cases, number, noun):
	url = "https://de.wiktionary.org/wiki/" + noun
	document = urlopen(url)
	print("downloading...." + url)
	content = document.read()
	soup = BeautifulSoup(content, 'html.parser')

	inflection_table = soup.find('table', {'class': 'wikitable'})

	if inflection_table:
		noun_rows = inflection_table.find_all('tr')[1:]

		nominativ = wikitionary_case_singular_plural_nouns(noun_rows[0])
		genitiv = wikitionary_case_singular_plural_nouns(noun_rows[1])
		dativ = wikitionary_case_singular_plural_nouns(noun_rows[2])
		akkusative = wikitionary_case_singular_plural_nouns(noun_rows[3])
		nouns = [
			list(zip(number, nominativ)),
			list(zip(number, genitiv)),
			list(zip(number, dativ)),
			list(zip(number, akkusative))
		]
	else:
		nouns = [(),(),(),()]

	return zip(cases, nouns)

if __name__ == "__main__":

	arguments = sys.argv[1:]

	if len(arguments) == 1:
		noun = arguments[0]
		source = "wiki"
	else:
		source = arguments[0]
		noun = arguments[1]

	print("trying to decline noun " + noun + " from source " + source)

	if source == "wiki":
		result = wiktionary_source(cases, number, noun)
	else:
		result = None

	print("here is result coming...", list(result) if result else None)
