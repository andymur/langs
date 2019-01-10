from bs4 import BeautifulSoup
import urllib2
import sys

if __name__ == "__main__":
	verb = sys.argv[1]
	document=urllib2.urlopen('http://conjugator.reverso.net/conjugation-german-verb-' + verb + '.html')
	content = document.read()
	#store it somewhere if needed
	#with open('document.html', 'w') as outputfile:
	#	outputfile.write(content)
	soup = BeautifulSoup(content, 'html.parser')
	divs = soup.find_all('div', {'class': 'wrap-three-col'})
	present_tense = divs[4]

	pronouns = ('ich', 'du', 'er_sie_es', 'wir', 'ihr', 'sie')
	verbs = []
	for item in present_tense.find_all('li'):
		verbs.append(item.find('i', {'class': 'verbtxt'}).get_text() + item.find('i', {'class': 'verbtxt-term'}).get_text())

	print(zip(pronouns, tuple(verbs)))
