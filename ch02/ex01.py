from urllib.request import urlopen
from bs4 import BeautifulSoup

result = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(result.read(), "html.parser")

spans = bsObj.findAll("span", {"class": "green"})

for span in spans:
    print(span.get_text())
