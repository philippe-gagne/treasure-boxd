from bs4 import BeautifulSoup
import requests
from lxml import html
import shlex

page = requests.get("https://letterboxd.com/philg2000/likes/films")
soup = BeautifulSoup(page.content, 'lxml')
mydivs = soup.findAll("div", {"class": "poster film-poster really-lazy-load"})

for div in mydivs:
    print(shlex.split(str(div))[3])
    print(shlex.split(str(div))[2])
    print("--------")




