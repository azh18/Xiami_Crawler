# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
import scrapy
from scrapy.pipelines.files import FilesPipeline
from scrapy.exceptions import DropItem

class XiamiTestPipeline(object):

    def open_spider(self, spider):
        self.artistJsonFile = codecs.open('artistJ.json','w+',buffering=100,encoding='utf-8')
        self.albumJsonFile = codecs.open('albumJ.json','w+',buffering=100,encoding='utf-8')
        self.songJsonFile = codecs.open('songJ.json','w+',buffering=100,encoding='utf-8')

    def close_spider(self, spider):
        self.artistJsonFile.close()
        self.albumJsonFile.close()
        self.songJsonFile.close()

    def process_item(self, item, spider):
        # The item is an artist
        if 'artistCommentNum' in item:
            line = json.dumps(dict(item)) + '\n'
            line = line.decode('unicode_escape')
            self.artistJsonFile.write(line)
            print('write a artist record')
            pass
        # item is an album
        if 'albumCommentNum' in item:
            line = json.dumps(dict(item)) + '\n'
            line = line.decode('unicode_escape')
            self.albumJsonFile.write(line)
            print('write a album record')
            pass
        # item is a song
        if 'songCommentNum' in item:
            line = json.dumps(dict(item)) + '\n'
            line = line.decode('unicode_escape')
            self.songJsonFile.write(line)
            print('write a song record')
            pass
        return item

class XiamiPipelineWithDownload(FilesPipeline):

    def get_media_requests(self, item, info):
        if 'file_urls' in item:
            yield scrapy.Request(item["file_urls"], meta={'id':item["songID"]})

    def file_path(self, request, response=None, info=None):
        songID = request.meta['id']
        songURL = request.url
        if "?" in songURL:
            file_guid = songID + '.' + songURL.split('?')[-2].split('.')[-1]
            filename = u'{0}'.format(file_guid)
        else:
            file_guid = songID + '.' + songURL.split('/')[-1].split('.')[-1]
            filename = u'{0}'.format(file_guid)
        return filename

