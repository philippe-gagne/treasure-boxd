from bs4 import BeautifulSoup as bs 
import requests
from lxml import html
import shlex
import math
import time

class Film:
    def __init__(self,title,slug,likers=[]):
        self.title = title
        self.slug = slug
        self.likers = likers

    def __repr__(self):
        return (self.title+" ("+self.slug+")")

    def __eq__(self, other): # override equals method (compare slugs)
        return (self.slug == other.slug)

    def getLikers(self): #TODO: write some general parser that gets passed page and what youre looking for so we dont have to keep copy pasting this (or read bs4 docs? hmm)
        
        page = requests.get("https://letterboxd.com/film/"+self.slug+"/likes/page/1/")
        soup = bs(page.content, 'lxml')

        num_of_likes = int(''.join((soup.find(name="a", attrs={"class":"tooltip", "href":"/film/"+self.slug+"/likes/"}).get("title")).split(u'\xa0')[0].split(","))) # Get amount of liked films for user as an int
        num_of_pages = math.ceil(num_of_likes/25)
        
        print(num_of_likes)
        print(num_of_pages)

        for i in range(1, num_of_pages+1):
            page = requests.get("https://letterboxd.com/film/"+self.slug+"/likes/page/"+str(i)+"/")
            soup = bs(page.content, 'lxml')
            mydivs = soup.find_all(name="a", attrs={"class":"name"})

            for div in mydivs:    
                self.likers.append(User(div.get("href").split("/")[1]))

class User:
    def __init__(self,user_id,liked_films=[]):  #this would all feel much nicer with just structs..
        self.user_id = user_id # user slug
        self.liked_films = [] #Array of films

    def __repr__(self):
        return self.user_id

    def __eq__(self, other):
        return self.user_id==other.user_id

    def getLikedFilms(self):
        page = requests.get("https://letterboxd.com/"+self.user_id+"/likes/films/page/1/")
        soup = bs(page.content, 'lxml')

        num_of_likes = int((soup.find(name="a", attrs={"class":"tooltip", "href":"/"+self.user_id+"/likes/films/"}).get("title")).split(u'\xa0')[0]) # Get amount of liked films for user as an int
        num_of_pages = math.ceil(num_of_likes/72)   # Amount of pages of likes there are

        if(num_of_likes==0):
            print("You have no liked movies")
        else:
            for x in range(1, num_of_pages+1):
                page = requests.get("https://letterboxd.com/"+self.user_id+"/likes/films/page/"+str(x)+"/") # get new page of liked movies
                soup = bs(page.content, 'lxml')

                liked_films_for_page = soup.find_all(name="div", class_= "film-poster") # find all movies on page

                for film_data in liked_films_for_page:
                    film_title = list(film_data.children)[1].get("alt") # extract film title
                    film_slug = film_data.get("data-film-slug").split("/")[2] #extract film slug
                    self.liked_films.append(Film(film_title, film_slug)) #add to user's list

    def getMutualLikes(self,other):
        temp = []
        for i in range(0,len(self.liked_films)):
            for j in range(0,len(other.liked_films)):
                if self.liked_films[i] == other.liked_films[j]:
                    temp.append(self.liked_films[i])
                    break
        return temp 

start = time.time()

phil = User("philg2000")
#ahmed = User("hahahahmed")
#ahmed.getLikedFilms()
phil.getLikedFilms()
#phil.liked_films[0].getLikers()
#print(ahmed.getMutualLikes(phil))

end = time.time()
total = end-start
print(total)   
