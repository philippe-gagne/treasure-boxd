import scrapy
import time

class User_LikedFilms_Spider(scrapy.Spider):
    name = 'user_likedfilms'
     
    __init__(self, user_slug):
        try:
            self.start_urls = ['https://letterboxd.com/'+user_slug+'/likes/films/page/1/']
        except:
            print("ERROR: No user slug provided")
            
        super().__init__(**kwargs)
    
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
            # }