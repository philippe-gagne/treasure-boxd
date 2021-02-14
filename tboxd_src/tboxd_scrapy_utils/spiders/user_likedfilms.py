import scrapy
import time

class User_LikedFilmsSpider(scrapy.Spider):

    name = 'user_likedfilms'
     
    def __init__(self, **kw):
        
        super(User_LikedFilmsSpider, self).__init__(**kw)

        try:
            slug = kw.get("slug") or kw.get("user_slug")
        except:
            print("No user slug provided")

        self.start_urls = ['https://letterboxd.com/'+slug+'/likes/films/page/1/']

    film_slugs = []
    film_titles = []
    film_data = {}

    def parse(self, response):
        start = time.time()

        film_slugs = response.css('div.poster.film-poster.really-lazy-load::attr(data-film-slug)').getall()
        film_titles = response.css('img.image::attr(alt)').getall()
        film_data = {}

        for i in range(0, len(film_slugs)):
            film_slugs[i] = film_slugs[i].split("/")[-2]
            film_data[film_slugs[i]] =  film_titles[i]
        
        end = time.time()
        total = end-start
        print(total)   

        print(film_data)
            
            # yield {
            #     'title' : poster.css('data-film-name').get()
            # 