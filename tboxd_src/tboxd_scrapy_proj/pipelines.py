# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from tboxd_scrapy_proj.items import UserLikesItem
from scrapy.exporters import CsvItemExporter
import csv

class UserLikesPipeline:

    def open_spider(self, spider):
        self.file = open('liked_films.csv', 'ab')
        self.exporter = CsvItemExporter(self.file)
        self.exporter.fields_to_export = ['username', 'film']
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
        self.exporter = CsvItemExporter(self.file)
        self.exporter.fields_to_export = ['username']

        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        item['username'] = item['username'][1:-1]
        self.exporter.export_item(item)
        return item