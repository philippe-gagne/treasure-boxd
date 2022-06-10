# gets all of the movies that the users scraped from film_likers.py liked

import json
import scrapy
from scrapy.crawler import CrawlerProcess, CrawlerRunner, Crawler
from tboxd_scrapy_proj.spiders import user_likedfilms, film_getuserlikes
import logging
import csv
import time
from twisted.internet import reactor, defer
logging.getLogger('scrapy').propagate = False

start_time = time.time()
print(start_time)

'''process = CrawlerProcess()


with open("users.csv") as myfile:
    firstNlines=myfile.readlines()[3:6] #temporarily hardcoded, can't call too many
    for line in firstNlines:
        swag = line.strip()
        print(swag)
        process.crawl(user_likedfilms.UserGetLikedFilmsSpider, user_slug=swag)

process.start()'''

runner = CrawlerRunner()

@defer.inlineCallbacks
def crawl():
    yield runner.crawl(user_likedfilms.UserGetLikedFilmsSpider, user_slug="philg2000")

    with open("liked_films.csv") as myfile:
        firstNlines=myfile.readlines()[3:6] #temporarily hardcoded, can't call too many
        for line in firstNlines:
            slug = line.strip().split(",")
            yield runner.crawl(film_getuserlikes.FilmGetUserLikesSpider, film_slug=slug[1], main_user="philg2000")

    with open("users.csv") as myfile:
        firstNlines=myfile.readlines()[3:6] #temporarily hardcoded, can't call too many
        for line in firstNlines:
            slug = line.strip()
            yield runner.crawl(user_likedfilms.UserGetLikedFilmsSpider, user_slug=slug)

    reactor.stop()

foo = open('users.csv', "w+", newline='')
writer = csv.writer(foo)
writer.writerow(['username'])
foo.close()

bar = open('liked_films.csv', 'w+', newline='')
writer = csv.writer(bar)
writer.writerow(['username','film'])
bar.close()

crawl()
reactor.run()

#get liked first 6400 liked users for each liked film [done]

#go through each user and write their likes to a new csv [done]


#TODO:
# - do all of the above but in 1 file/1 go
# - load all of the csv data into a scipy sparse matrix 
# - (optional?) move all of the data into a database 
# - actually generate the recommendations
#pass that csv to recco

print("script finished: "+ str(time.time() - start_time)+" seconds")