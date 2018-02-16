from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import ssl


class Page:
    def __init__(self, title, paragraph, link="", url=""):
        self.title = title
        self.paragraph = paragraph
        self.link = link
        self.url = url

    def __str__(self):
        return "title=" + self.title + "\nparagraph=" + self.paragraph \
               + "\nlink=" + self.link + "\nurl=" + self.url + "\n"


def recursive(url):
    context = ssl._create_unverified_context()
    print("url :: " + url)
    result = urlopen("https://en.wikipedia.org" + url, context=context)
    bsObj = BeautifulSoup(result.read(), "html.parser")

    title = bsObj.h1.get_text()
    paragraph = bsObj.find("div", {"id": "mw-content-text"}).find("p").get_text()
    link = ""
    if bsObj.find("li", {"id": "ca-edit"}) is not None:
        link = bsObj.find("li", {"id": "ca-edit"}).find("span").find("a").attrs["href"]

    page = Page(title, paragraph, link, url)
    print(page)

    tags = bsObj.find("div", {"id": "bodyContent"}) \
        .findAll("a", href=re.compile("^(?:/wiki/)[^:.]*$"))

    for tag in tags:
        href = tag.attrs["href"]
        if tag.attrs["href"] not in urls:
            urls.add(href)
            recursive(href)


urls = set()
recursive("/wiki/Kevin_Bacon")
