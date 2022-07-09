from bs4 import BeautifulSoup
import requests

animalsCount = {}
url = 'https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83'


def main(url):
    q = requests.get(url)
    soup = BeautifulSoup(q.content, 'html.parser')

    rootNode = soup.find('div', id='mw-pages')
    letters = rootNode.find_all('div', class_='mw-category-group')

    for letterNode in letters:
        letter = letterNode.find("h3").text
        if not letter in animalsCount:
            animalsCount[letter] = 0
        animalsCount[letter] += len(letterNode.find_all('li'))

    nextPageNode = rootNode.find('a', string="Следующая страница")
    if nextPageNode:
        return 'https://ru.wikipedia.org/' + nextPageNode.get("href")
    return None


nextPageLink = url
while True:
    nextPageLink = main(nextPageLink)
    print(nextPageLink)
    print(animalsCount)
    if nextPageLink is None:
        break

print(animalsCount)