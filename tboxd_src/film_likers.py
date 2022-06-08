# gets all the people that liked movies that main_user also liked


import json
import scrapy
from scrapy.crawler import CrawlerProcess, CrawlerRunner, Crawler
from tboxd_scrapy_proj.spiders import user_likedfilms, film_getuserlikes
import logging
import csv
import time
logging.getLogger('scrapy').propagate = False

start_time = time.time()
print(start_time)



# opens csv to to write usernames of other users
with open('users.csv', 'w', newline='') as usercsv:
    fieldnames=['username']
    user_writer = csv.DictWriter(usercsv, fieldnames=fieldnames)
    user_writer.writeheader()




def crawlem():
    get_films_liked_users = CrawlerProcess()
    with open("liked_films.csv") as myfile:
        firstNlines=myfile.readlines()[3:6] #temporarily hardcoded, can't call too many
        for line in firstNlines:
            slug = line.strip().split(",")
            get_films_liked_users.crawl(film_getuserlikes.FilmGetUserLikesSpider, film_slug=slug[1], main_user="philg2000")
        get_films_liked_users.start()
        get_films_liked_users._graceful_stop_reactor



print("script finished: "+ str(time.time() - start_time)+" seconds")