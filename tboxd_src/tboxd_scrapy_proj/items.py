# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class UserLikesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    film = scrapy.Field()

class MutualLikersItem(scrapy.Item):
    film = scrapy.Field()
    username = scrapy.Field()