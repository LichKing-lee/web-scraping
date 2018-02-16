from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

result = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(result.read(), "html.parser")

# print(bsObj.findAll("img"))
print(bsObj.findAll("img", {"src": re.compile("../img/gifts/img[0-9].jpg")}))