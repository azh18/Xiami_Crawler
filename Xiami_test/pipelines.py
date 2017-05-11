# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs

class XiamiTestPipeline(object):

    def open_spider(self, spider):
        self.artistJsonFile = codecs.open('artistJ.json','w+',buffering=1000,encoding='utf-8')
        self.albumJsonFile = codecs.open('albumJ.json','w+',buffering=1000,encoding='utf-8')
        self.songJsonFile = codecs.open('songJ.json','w+',buffering=1000,encoding='utf-8')

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
