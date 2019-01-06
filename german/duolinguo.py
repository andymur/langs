from bs4 import BeautifulSoup

if __name__ == "__main__":
    input_filename = "duolinguo_words.txt"

    soup = None

    with open(input_filename) as input_file:
        content = input_file.read()
        soup = BeautifulSoup(content, 'html.parser')
    #print(soup.prettify())
    all_spans = soup.find_all('span')
    for span in all_spans:
        word_or = span.get_text()
        if len(word_or) > 0 and len(word_or) < 20:
            pass #print(word_or)
        elif len(word_or):
            print(word_or)
    #print(first_row.span)
    #print(first_row.span.get_text())
    #for tr in soup.find_all('tr')[3:]:
    #    print(tr)
