import scrapy
import logging
import csv

class FilmGetUserLikesSpider(scrapy.Spider):
    name = 'film_getuserlikes'
    allowed_domains = ['letterboxd.com']
    start_urls = ['https://letterboxd.com/film/enemy/likes/page/1/']
    user_num = None
    all_users = []
    logging.getLogger('scrapy').propagate = True

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

        for x in range(0, len(user_slugs)):
            user_slugs[x] = user_slugs[x][1:-1]

        if self.main_user in user_slugs: user_slugs.remove(self.main_user)
        self.all_users = self.all_users + user_slugs



        # if(like_num / 25 >= 256):
        #     page_num = 256
        # else:
        #     page_num = (like_num / 25) + 1

        if response.css('a.previous').get() == None :
            for x in range(2, 257):
                yield scrapy.Request(url='https://letterboxd.com/film/'+self.film_slug+'/likes/page/'+str(x)+'/')


    def close(self, reason):
        with open('users.csv', 'a', newline='') as outfile:
            fieldnames=['username']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            for user in self.all_users:
                writer.writerow({'username':user})

