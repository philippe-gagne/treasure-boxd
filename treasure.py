from bs4 import BeautifulSoup
import requests
from lxml import html
import shlex
import math

class Film:
    def __init__(self,title,slug):
        self.title = title
        self.slug = slug

    def __str__(self):
        return (self.title+" ("+self.slug+")")

    def __str__(self):
        return (self.title+" ("+self.slug+")")

class Profile:
    def __init__(self,user_id,liked_films):  #this would all feel much nicer with just structs..
        self.user_id = user_id
        self.liked_films = []


profile = Profile(user_id="philg2000", liked_films=[])

page = requests.get("https://letterboxd.com/"+profile.user_id+"/likes/films/page/1/")
soup = BeautifulSoup(page.content, 'lxml')

num_of_likes = int((soup.find(name="a", attrs={"class":"tooltip", "href":"/"+profile.user_id+"/likes/films/"}).get("title")).split(u'\xa0')[0]) # Get amount of liked films for user as an int
num_of_pages = math.ceil(num_of_likes/72)   # Amount of pages of likes there are

print("Liked movies: " + str(num_of_likes))
print("Pages of liked movies: "+str(num_of_pages))

if(num_of_likes==0):
    print("You have no liked movies")
else:
    for x in range(1, num_of_pages+1):
        page = requests.get("https://letterboxd.com/"+profile.user_id+"/likes/films/page/"+str(x)+"/") # get new page of liked movies
        soup = BeautifulSoup(page.content, 'lxml')

        liked_films_for_page = soup.find_all(name="div", class_= "film-poster") # find all movies on page

        for film_data in liked_films_for_page:
            film_title = list(film_data.children)[1].get("alt") # extract film title
            film_slug = film_data.get("data-film-slug").split("/")[2] #extract film slug
            profile.liked_films.append(Film(film_title, film_slug)) #add to user's list

for movie in profile.liked_films:
    print(movie)

    
#mydivs = soup.findAll("div", {"class": "poster film-poster really-lazy-load"})


#for div in mydivs: #TODO: get rid of shlex, very lazy hack. im pretty sure bs4 has something built in to do what im trying to do
#    temp = shlex.split(str(div))    
#    name = temp[3].split("/")[2]
#    num = temp[2].split("=")[1]
#    profile.movies.append(Film(name,num))

#print(profile.movies[0].name)