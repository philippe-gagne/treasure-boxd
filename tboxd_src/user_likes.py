#gets all of the films that main_user liked and writes them to liked_films.csv

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
    film_writer.writeheader() #is this even needed

def crawlem(user="philg2000", nearby=True):
    process = CrawlerProcess()
    process.crawl(user_likedfilms.UserGetLikedFilmsSpider, user_slug=user)
    process.start()


print("script finished: "+ str(time.time() - start_time)+" seconds")
