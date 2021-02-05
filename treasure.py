from bs4 import BeautifulSoup
import requests
from lxml import html
import shlex


class Film:
    def __init__(self,name,num,likers=[]):
        self.name = name
        self.num = num 
        self.likers=likers
    
    def getLikers(self): #TODO: write some general parser that gets passed page and what youre looking for so we dont have to keep copy pasting this (or read bs4 docs? hmm)
        page = requests.get("https://letterboxd.com/film/"+self.name+"/likes")
        soup = BeautifulSoup(page.content, 'lxml')
        mydivs = soup.findAll("div", {"class": "person-summary"})
        for div in mydivs: 
            temp = shlex.split(str(div))  
            name = temp[4].split("/")[1]
            self.likers.append(name)  

class Profile:
    def __init__(self,name,likes=[]):  #this would all feel much nicer with just structs..
        self.name = name
        self.likes = likes
    def getlikes(self):
        page = requests.get("https://letterboxd.com/"+self.name+"/likes/films")
        soup = BeautifulSoup(page.content, 'lxml')
        mydivs = soup.findAll("div", {"class": "poster film-poster really-lazy-load"})
        for div in mydivs: #TODO: get rid of shlex, very lazy hack. im pretty sure bs4 has something built in to do what im trying to do
            temp = shlex.split(str(div))    
            name = temp[3].split("/")[2]
            num = temp[2].split("=")[1]
            self.likes.append(Film(name,num))


#likes
#seen
#watchlist? 


profile = Profile("hahahahmed")
profile.getlikes()
profile.likes[3].getLikers() #wolf of wall street :3 
print(profile.likes[3].likers)
