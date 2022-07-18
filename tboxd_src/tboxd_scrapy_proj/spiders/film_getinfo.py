import scrapy
import logging
import csv
from tboxd_scrapy_proj.items import MovieItem

class FilmGetInfoSpider(scrapy.Spider):
    name = 'film_getnanogenres'
    allowed_domains = ['letterboxd.com']
    start_urls = ['https://letterboxd.com/film/enemy/']
    logging.getLogger('scrapy').propagate = False

    custom_settings = {
        'ITEM_PIPELINES':{
            'tboxd_scrapy_proj.pipelines.FilmInfoPipeline': 300
        }
    }

    def __init__(self, film_slug='enemy', score=0, **kwargs):
        '''
        Spider that crawls a film's page and collects info about the film.

        :param film_slug: movie's internal name, as shown in the url of the page
        :type film_slug: string
        :param score: movie's recommendation score
        :type score: int
        :param kw: keyword arguments to initialize Spider
        ''' 
        # global all_users        
        self.film_slug = film_slug
        self.start_urls = ['https://letterboxd.com/film/'+film_slug+'/']
        self.score = score
        super().__init__(**kwargs)

    def parse(self, response):
        
        item = MovieItem()

        item['movie'] = self.film_slug
        item['score'] = self.score
        item['title'] = response.xpath("//div[@id='content']/div[@class='content-wrap']/div[@id='film-page-wrapper']/div[@class='col-17']/section[@id='featured-film-header']/h1[@class='headline-1 js-widont prettify']/text()").get()
        item['year'] = response.xpath("//div[@id='content']/div[@class='content-wrap']/div[@id='film-page-wrapper']/div[@class='col-17']/section[@id='featured-film-header']/p/small[@class='number']/a/text()").get()
        item['director'] = response.xpath("//div[@id='content']/div[@class='content-wrap']/div[@id='film-page-wrapper']/div[@class='col-17']/section[@id='featured-film-header']/p/a/span[@class='prettify']/text()").get()
        item['runtime'] = response.xpath("//div[@class='content-wrap']/div[@id='film-page-wrapper']/div[@class='col-17']/section[@class='section col-10 col-main']/p[@class='text-link text-footer']/text()").get().replace("\t","").replace("\n", "").replace("\xa0", " ").split()[0]
        item['rating'] = response.xpath("//html[@id='html']/head/meta[@name='twitter:data2']/@content").get().split()[0]
        item['ratingcount'] = response.xpath("//script[@type='application/ld+json']/text()").get().split("ratingCount")[1].split(",")[0][2:]
        
        #genres
        #views
        #likes

        yield item