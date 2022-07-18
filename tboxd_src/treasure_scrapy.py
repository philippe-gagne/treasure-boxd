# gets all of the movies that the users scraped from film_likers.py liked

import json
import scrapy
from scrapy.crawler import CrawlerProcess, CrawlerRunner, Crawler
from tboxd_scrapy_proj.spiders import user_likedfilms, film_getnanogenres, film_getinfo
import logging
import csv
import time
from twisted.internet import reactor, defer
logging.getLogger('scrapy').propagate = False

start_time = time.time()
print(start_time)

runner = CrawlerRunner()  

@defer.inlineCallbacks
def crawl():

    #get user's watched and liked films
    yield runner.crawl(user_likedfilms.UserGetLikedFilmsSpider, user_slug="philg2000")

    #goes through user's watched films and gets the nanogenres for liked films
    with open("liked_films.csv") as myfile:
        firstNlines=myfile.readlines()
        for line in firstNlines:
            data = line.strip().split(",")
            viewed_films.append(data[0])
            if data[1] == 'true':
                # print(slug)
                yield runner.crawl(film_getnanogenres.FilmGetNanogenresSpider, film_slug=data[0])

    # count how much each nanogenre recurrs
    with open("nanogenres.csv") as myfile:
        firstNlines=myfile.readlines()[1:-1]
        top_themes = {}
        for line in firstNlines:
            theme = line.strip().split(",")
            if theme[0] in top_themes:
                top_themes[theme[0]] += 1
            else:
                top_themes[theme[0]] = 1
    
    # count how much each movie recurrs across all nanogenres)
    with open("movies.csv") as myfile:
        firstNlines=myfile.readlines()[1:-1]
        top_movies = {}
        for line in firstNlines:
            movie = line.strip().split(",")[1]
            if movie in top_movies:
                top_movies[movie] += 1
            else:
                top_movies[movie] = 1


    sorted_top_themes = sorted(top_themes.items(), key=lambda x: x[1], reverse=True)

    for film in viewed_films:
        top_movies.pop(film, None)

    sorted_top_movies = sorted(top_movies.items(), key=lambda x: x[1], reverse=True)

    # produce_recommendations(top_themes=sorted_top_themes, top_movies = sorted_top_movies)
    top_movie_list = list(sorted_top_movies)
    for x in range(50):
        film = top_movie_list[x]
        yield runner.crawl(film_getinfo.FilmGetInfoSpider, film_slug=film[0], score=int(film[1]))

    reactor.stop()

def produce_recommendations(top_themes, top_movies):
    pass
    # for x in range(50):
    #     film = list(top_movies)[x]
    #     print(film[0], film[1])
    #     yield runner.crawl(film_getinfo.FilmGetInfoSpider, film_slug=film[0], score=int(film[1]))  


foo = open('nanogenres.csv', "w+", newline='')
writer = csv.writer(foo)
writer.writerow(['theme'])
foo.close()

foo = open('movies.csv', "w+", newline='')
writer = csv.writer(foo)
writer.writerow(['theme', 'movie'])
foo.close()

bar = open('liked_films.csv', 'w+', newline='')
writer = csv.writer(bar)
writer.writerow(['film', 'liked'])
bar.close()

foo = open('recommendations.csv', "w+", newline='')
writer = csv.writer(foo)
writer.writerow(['movie','score','title','year','director','runtime','rating','ratingcount'])
foo.close()

viewed_films = []

crawl()
reactor.run()

#TODO:
# - do all of the above but in 1 file/1 go
# - load all of the csv data into a scipy sparse matrix 
# - (optional?) move all of the data into a database 
# - actually generate the recommendations
#pass that csv to recco

print("script finished: "+ str(time.time() - start_time)+" seconds")