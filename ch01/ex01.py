from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup


def parseAndPrint(html):
    print(html)
    bsObj = BeautifulSoup(html, "html.parser")
    print(bsObj)


try:
    result = urlopen("http://www.pythonscraping.com/pages/error.html")
except HTTPError as e:
    print(e)
else:
    parseAndPrint(result.read())
