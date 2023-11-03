# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import logging, os

import pymongo
import sqlite3

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), override=True)

class MongodbPipeline:
    collenction_name = 'transcripts'
    
    def open_spider(self, spider):
        self.client =  pymongo.MongoClient(os.environ.get("MONGODB_URI"))
        self.db = self.client['My_Database']
        
    def close_spider(self, spider):
        self.client.close()
    
    def process_item(self, item, spider):
        self.db[self.collenction_name].insert_one(item)
        return item


class SQLitePipeline:
    def create_database(self):
        connection = sqlite3.connect("transcripts.db")
        c = connection.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS transcripts(
                title TEXT,
                plot TEXT,
                transcript TEXT,
                url TEXT
            )
        ''')
        connection.commit()
        connection.close()

    def open_spider(self, spider):
        self.create_database()
        self.connection = sqlite3.connect("transcripts.db")
        self.c = self.connection.cursor()
        
    def close_spider(self, spider):
        self.connection.close()
    
    def process_item(self, item, spider):
        self.c.execute('''
                       INSERT INTO transcripts (title, plot, transcript, url) VALUES(?, ?, ?, ?)
                       ''', (
                           item.get('title'),
                           item.get('plot'),
                           item.get('transcript'),
                           item.get('url'),
                       ))
        self.connection.commit()
        
        return item
    