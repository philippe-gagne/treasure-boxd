import scrapy
from scrapy.crawler import CrawlerProcess, CrawlerRunner
import treasureboxd.spiders

process = CrawlerProcess()
process.crawl(user_likedfilms("philg2000"))