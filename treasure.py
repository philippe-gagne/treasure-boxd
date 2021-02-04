from bs4 import BeautifulSoup
import requests
from lxml import html
import shlex


class Film:
    def __init__(self,name,num):
        self.name = name
        self.num = num 

class Profile:
    def __init__(self,name,movies=[]):  #this would all feel much nicer with just structs..
        self.name = name
        self.movies = movies

profile = Profile("philg2000")

page = requests.get("https://letterboxd.com/"+profile.name+"/likes/films")
soup = BeautifulSoup(page.content, 'lxml')
mydivs = soup.findAll("div", {"class": "poster film-poster really-lazy-load"})

for div in mydivs: #TODO: get rid of shlex, very lazy hack. im pretty sure bs4 has something built in to do what im trying to do
    temp = shlex.split(str(div))    
    name = temp[3].split("/")[2]
    num = temp[2].split("=")[1]
    profile.movies.append(Film(name,num))

print(profile.movies[0].name)
