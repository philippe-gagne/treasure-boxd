import scrapy
import logging
import csv
from tboxd_scrapy_proj.items import MutualLikersItem

class FilmGetUserLikesSpider(scrapy.Spider):
    name = 'film_getuserlikes'
    allowed_domains = ['letterboxd.com']
    start_urls = ['https://letterboxd.com/film/enemy/likes/page/1/']
    user_num = None
    all_users = []
    logging.getLogger('scrapy').propagate = False

    custom_settings = {
        'ITEM_PIPELINES':{
            'tboxd_scrapy_proj.pipelines.MutualLikersPipeline': 300
        }
    }

    def __init__(self, film_slug='enemy', main_user='philg2000', **kwargs):
        '''
        Spider that crawls a film's page to collect every user that has "Liked" that film.

        :param film_slug: movie's internal name, as shown in the url of the page
        :type film_slug: string
        :param kw: keyword arguments to initialize Spider
        ''' 
        # global all_users        
        self.film_slug = film_slug
        self.start_urls = ['https://letterboxd.com/film/'+film_slug+'/likes/page/1/']
        self.all_users = []
        self.main_user = main_user
        super().__init__(**kwargs)

    def parse(self, response):

        user_slugs = response.css('a.name::attr(href)').getall()

        like_num = response.css('li.js-route-likes').xpath('a/@title').get()
        like_num = int(like_num.split('\xa0')[0].replace(',',''))

        item = MutualLikersItem()
        for user in user_slugs:
            item['username'] = user
            yield item

        if response.css('a.previous').get() == None :
            for x in range(2, 257):
                yield scrapy.Request(url='https://letterboxd.com/film/'+self.film_slug+'/likes/page/'+str(x)+'/')
