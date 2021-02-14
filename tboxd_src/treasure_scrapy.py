import scrapy
from scrapy.crawler import CrawlerProcess, CrawlerRunner
#import scrapy_utils.spiders as project_spiders

process = CrawlerProcess()
process.crawl("user_likedfilms", user_slug="philg2000")


#project_spiders.("user_likedfilms"), user_slug="philg2000"