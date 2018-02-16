from urllib.request import urlopen
from bs4 import BeautifulSoup

result = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(result.read(), "html.parser")

print(bsObj.find(attrs={"class": "green"}))