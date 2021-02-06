from bs4 import BeautifulSoup as bs 
import requests
from lxml import html
import shlex


class Film:
    def __init__(self,name,num,likers=[]):
        self.name = name
        self.num = num 
        self.likers=likers
    
    def __toString__(self):
        return self.name

    def getLikers(self): #TODO: write some general parser that gets passed page and what youre looking for so we dont have to keep copy pasting this (or read bs4 docs? hmm)
        page = requests.get("https://letterboxd.com/film/"+self.name+"/likes")
        soup = bs(page.content, 'lxml')
        mydivs = soup.findAll("div", {"class": "person-summary"})
        for div in mydivs: 
            temp = shlex.split(str(div))  
            name = temp[4].split("/")[1]
            self.likers.append(name)  

class Profile:
    def __init__(self,name):  #this would all feel much nicer with just structs..
        self.name = name
        self.likes = []
    def getlikes(self):
        page = requests.get("https://letterboxd.com/"+self.name+"/likes/films")
        soup = bs(page.content, 'lxml')
        mydivs = soup.findAll("div", {"class": "poster film-poster really-lazy-load"})
        for div in mydivs: #TODO: get rid of shlex, very lazy hack. im pretty sure bs4 has something built in to do what im trying to do
            temp = shlex.split(str(div))    
            name = temp[3].split("/")[2]
            num = temp[2].split("=")[1]
            self.likes.append(Film(name,num))
    def getMutualLikes(self,other):
        temp = []
        for i in range(0,len(self.likes)): #overload the equality operator in the film class and this should become shorter (just check liked in other.likes)
            for j in range(0,len(other.likes)):
                if self.likes[i].name == other.likes[j].name:
                    temp.append(self.likes[i])
        return temp 
    

    
'''
profile.likes[3].getLikers() #wolf of wall street :3 
array = []
for liker in profile.likes[3].likers:
    temp = Profile(liker)
    temp.getlikes()
    array.append(temp)
    
print(array[3].name)
print(array[3].likes[4].name)
'''


#likes
#seen
#watchlist? 

ahmed = Profile("hahahahmed")
phil = Profile("philg2000")
ahmed.getlikes()
phil.getlikes()

print(ahmed.getMutualLikes(phil))
