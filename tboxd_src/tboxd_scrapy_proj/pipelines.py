# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from tboxd_scrapy_proj.items import UserLikesItem, MovieAndThemeItem, ThemeItem
from scrapy.exporters import CsvItemExporter
import csv

class UserLikesPipeline:

    def open_spider(self, spider):
        self.file = open('liked_films.csv', 'ab')
        self.exporter = CsvItemExporter(self.file, include_headers_line = False)
        self.exporter.fields_to_export = ['film', 'liked']
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
    
    def process_item(self, item, spider):
        item['film'] = item['film'].split("/")[-2]
        self.exporter.export_item(item)
        return item

class MutualLikersPipeline:

    def open_spider(self, spider):
        self.file = open('users.csv', 'ab')
        self.exporter = CsvItemExporter(self.file, include_headers_line=False)
        self.exporter.fields_to_export = ['username']
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        item['username'] = item['username'][1:-1]
        self.exporter.export_item(item)
        return item

class NanogenresPipeline:

    def open_spider(self, spider):
        self.genresfile = open('nanogenres.csv', 'ab')
        self.moviesfile = open('movies.csv', 'ab')

        self.genresexporter = CsvItemExporter(self.genresfile, include_headers_line=False)
        self.moviesexporter = CsvItemExporter(self.moviesfile, include_headers_line=False)

        self.genresexporter.fields_to_export = ['theme']

        self.moviesexporter.fields_to_export = ['theme', 'movie']

        self.genresexporter.start_exporting()
        self.moviesexporter.start_exporting()
    
    def close_spider(self, spider):
        self.genresexporter.finish_exporting()
        self.moviesexporter.finish_exporting()
        self.genresfile.close()
        self.moviesfile.close()
    
    def process_item(self, item, spider):
        item['theme'] = item['theme'].split("/")[3]
        if isinstance(item, ThemeItem):
            self.genresexporter.export_item(item)
        elif isinstance(item, MovieAndThemeItem):
            item['movie'] = item['movie'].split("/")[2]
            self.moviesexporter.export_item(item)
        return item

class FilmInfoPipeline:

    def open_spider(self, spider):
        self.file = open('recommendations.csv', 'ab')
        self.exporter = CsvItemExporter(self.file, include_headers_line=False)
        self.exporter.fields_to_export = ['movie','score','title','year','director','runtime','rating','ratingcount']
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item