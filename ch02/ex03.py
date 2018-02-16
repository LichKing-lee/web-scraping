from urllib.request import urlopen
from bs4 import BeautifulSoup

result = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(result.read(), "html.parser")

for gift in bsObj.find("table", {"id": "giftList"}).children:
    print(gift)