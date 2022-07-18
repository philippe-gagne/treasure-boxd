import scrapy
import logging
import csv
from tboxd_scrapy_proj.items import ThemeItem, MovieAndThemeItem

class FilmGetNanogenresSpider(scrapy.Spider):
    name = 'film_getnanogenres'
    allowed_domains = ['letterboxd.com']
    start_urls = ['https://letterboxd.com/film/enemy/nanogenres/']
    user_num = None
    all_users = []
    logging.getLogger('scrapy').propagate = False

    custom_settings = {
        'ITEM_PIPELINES':{
            'tboxd_scrapy_proj.pipelines.NanogenresPipeline': 300
        }
    }

    def __init__(self, film_slug='enemy', **kwargs):
        '''
        Spider that crawls a film's page to get all its nanogenres and the top 16 movies that belong to each nanogenre.

        :param film_slug: movie's internal name, as shown in the url of the page
        :type film_slug: string
        :param kw: keyword arguments to initialize Spider
        ''' 
        # global all_users        
        self.film_slug = film_slug
        self.start_urls = ['https://letterboxd.com/film/'+film_slug+'/nanogenres/']
        super().__init__(**kwargs)

    def parse(self, response):

        theme_slugs = response.css('h2').css('a::attr(href)').getall()

        item = ThemeItem()
        for url in theme_slugs:
            item['theme'] = url
            yield item

        item = MovieAndThemeItem()
        if(len(theme_slugs) > 0):
            movie_slugs = response.xpath("//div[@id='content']/div[@class='content-wrap']/div[@class='cols-2']/section[@class='section col-17 col-main']/section[@class='section genre-group']/ul[@class='poster-list -p70 -horizontal -grid -fillrow']/li").css('li::attr(data-film-slug)').getall()

            for i in range(len(movie_slugs)):
                item['movie'] = movie_slugs[i]
                theme = i // 16
                item['theme'] = theme_slugs[theme]
                yield item