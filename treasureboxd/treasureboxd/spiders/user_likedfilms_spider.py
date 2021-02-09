import scrapy

class User_LikedFilms_Spider(scrapy.Spider):

    name = 'user_likedfilms'
    start_urls = ['https://letterboxd.com/philg2000/likes/films/page/1/']

    film_slugs = []
    film_titles = []
    film_data = {}

    def parse(self, response):


        film_slugs = response.css('div.poster.film-poster.really-lazy-load::attr(data-film-slug)').getall()
        film_titles = response.css('img.image::attr(alt)').getall()
        film_data = {}

        for i in range(0, len(film_slugs)):
            film_slugs[i] = film_slugs[i].split("/")[-2]
            film_data[film_slugs[i]] =  film_titles[i]
        
        print(film_data)
            
            # yield {
            #     'title' : poster.css('data-film-name').get()
            # }
    