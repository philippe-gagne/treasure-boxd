# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class UserLikesItem(scrapy.Item):
    # define the fields for your item here like:
    film = scrapy.Field()
    liked = scrapy.Field()

class MutualLikersItem(scrapy.Item):
    # film = scrapy.Field()
    username = scrapy.Field()

class ThemeItem(scrapy.Item):
    theme = scrapy.Field()

class MovieAndThemeItem(scrapy.Item):
    theme = scrapy.Field()
    movie = scrapy.Field()

class MovieItem(scrapy.Item):
    movie = scrapy.Field()
    score = scrapy.Field()
    title = scrapy.Field()
    year = scrapy.Field()
    director = scrapy.Field()
    runtime = scrapy.Field()
    rating = scrapy.Field()
    ratingcount =  scrapy.Field()
    # genres = scrapy.Field()
    # views = scrapy.Field()
    # likes = scrapy.Field()
