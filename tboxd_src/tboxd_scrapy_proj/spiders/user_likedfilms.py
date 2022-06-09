import scrapy
import csv
import time
import logging

logging.getLogger('scrapy').propagate = True


class UserGetLikedFilmsSpider(scrapy.Spider):

    name = 'user_likedfilms'
    allowed_domains = ['letterboxd.com']
    start_urls = ['https://letterboxd.com/philg2000/likes/films/page/1/']  

    def __init__(self, user_slug="philg2000", **kwargs):
        '''
        Spider that crawls a user's profile to get all their 'Liked' films.

        :param user_slug: given user's username, as shown in the url of their profile
        :type user_slug: string
        :param kw: keyword arguments to initialize Spider
        '''
        self.user_slug = user_slug
        self.start_urls = ['https://letterboxd.com/'+self.user_slug+'/likes/films/page/1/']

        super().__init__(**kwargs) 

    def parse(self, response):
        '''
        Scrapes all the films from the user profile and returns all the film slugs (ids)

        @return: array of film slugs as strings
        '''
        if response.css('a.previous').get() == None:
            like_num = response.css('li.selected').xpath('a/@title').get()
            like_num = int(like_num.split('\xa0')[0].replace(',',''))

            if(like_num%72 == 0):
                page_num = like_num // 72
            else:
                page_num = (like_num // 72)+1
            

        film_slugs = response.css('div.poster.film-poster.really-lazy-load::attr(data-film-slug)').getall()
        for i in range(len(film_slugs)):
            film_slugs[i] = film_slugs[i].split("/")[-2]

        with open("liked_films.csv", "a", newline="") as outfile:
            fieldnames = ["user","film"]
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            for film in film_slugs:
                writer.writerow({'user' : self.user_slug,'film' : film})


        # if response.css('a.previous').get() == None and page_num > 1 :
        #     for x in range(2, (page_num+1)):
        #         yield scrapy.Request(url='https://letterboxd.com/'+self.user_slug+'/likes/films/page/'+str(x)+'/')
