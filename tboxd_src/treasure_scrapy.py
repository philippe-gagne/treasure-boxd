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

with open('liked_films.csv', 'w', newline='') as filmcsv:
    fieldnames=['film']
    film_writer = csv.DictWriter(filmcsv, fieldnames=fieldnames)
    film_writer.writeheader()

# opens user profile and gets their liked films and writes them to a csv
get_user_liked_films = CrawlerProcess()
get_user_liked_films.crawl(user_likedfilms.UserGetLikedFilmsSpider, user_slug="philg2000")
get_user_liked_films.start()
get_user_liked_films._graceful_stop_reactor()

# opens csv to to write usernames of other users
with open('users.csv', 'w', newline='') as usercsv:
    fieldnames=['username']
    user_writer = csv.DictWriter(usercsv, fieldnames=fieldnames)
    user_writer.writeheader()

get_films_liked_users = CrawlerProcess()

# time.sleep(5)

# test_list = ['enemy','parasite-2019','blade-runner-2049','the-master-2012']
# for film in test_list:
#     get_films_liked_users.crawl(film_getuserlikes.FilmGetUserLikesSpider, film_slug=film, main_user="philg2000")

with open('liked_films.csv', newline='') as liked_films_file:
    film_reader = csv.reader(liked_films_file, delimiter=' ', quotechar='|')
    for row in film_reader:
        print(row[0])
        if row[0] != 'film':
            get_films_liked_users.crawl(film_getuserlikes.FilmGetUserLikesSpider, film_slug=row[0], main_user="philg2000")

# get_films_liked_users.start()

#get liked first 6400 liked users for each liked film

#go through each user and write their likes to a new csv
#pass that csv to recco

print("script finished: "+ str(time.time() - start_time)+" seconds")