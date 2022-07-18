import scrapy
import csv
import time
import logging
from tboxd_scrapy_proj.items import UserLikesItem

logging.getLogger('scrapy').propagate = True


class UserGetLikedFilmsSpider(scrapy.Spider):

    name = 'user_likedfilms'
    allowed_domains = ['letterboxd.com']
    start_urls = ['https://letterboxd.com/philg2000/films/page/1/'] 

    custom_settings = {
        'ITEM_PIPELINES':{
            'tboxd_scrapy_proj.pipelines.UserLikesPipeline': 300
        }
    }

    def __init__(self, user_slug="philg2000", **kwargs):
        '''
        Spider that crawls a user's profile to get all their 'Liked' films.

        :param user_slug: given user's username, as shown in the url of their profile
        :type user_slug: string
        :param kw: keyword arguments to initialize Spider
        '''
        self.user_slug = user_slug
        self.start_urls = ['https://letterboxd.com/'+self.user_slug+'/films/page/1/']

        super().__init__(**kwargs) 

    def parse(self, response):
        '''
        Scrapes all the films from the user profile and returns all the film slugs in a csv

        @return: array of film slugs as strings
        '''

        films = response.xpath("//div[@id='content']/div[@class='content-wrap']/div[@class='cols-2 overflow']/section[@class='section col-main overflow']/ul[@class='poster-list -p70 -grid film-list clear']/li")

        item = UserLikesItem()
        for film in films:
            item['film'] = film.css('div::attr(data-film-slug)').get()
            if film.xpath(".//span[@class='icon']").get() == None:
                item['liked'] = 'false'
            else:
                item['liked'] = 'true'
            yield item

        next_url = response.xpath("//div[@id='content']/div[@class='content-wrap']/div[@class='cols-2 overflow']/section[@class='section col-main overflow']/div[@class='pagination']/div[@class='paginate-nextprev']/a[@class='next']").css('a::attr(href)').get()
        
        if next_url != None:
            yield scrapy.Request(url='https://letterboxd.com/'+next_url)