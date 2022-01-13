from bs4 import BeautifulSoup

def parseFile(filename):
    with open(filename, 'r') as f:
        html_text = f.read()
    soup = BeautifulSoup(html_text, 'html.parser')

    german_words = []
    english_words = []

    for s in soup.find_all("div", {"class": "col_a col text"}):
        german_words.append(s.text)
    
    for s in soup.find_all("div", {"class": "col_b col text"}):
        english_words.append(s.text)

    assert(len(german_words) == len(english_words))

    words = []
    for i in range(0,len(german_words)):
        words.append({'german': german_words[i], 'english': english_words[i]})
    return words


def printParse(words):
    for word in words:
        print(word["german"], end="\t")
        print(word["english"], end="\t")
        print("")


def main():
    for i in range(1, 338+1):
        words = parseFile("./html_data/" + str(i) + ".html")
        printParse(words)

main()