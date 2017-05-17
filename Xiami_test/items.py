# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

'''
The defination can be found in my note in YouDao
'''


class XiamiArtistItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    artistName = scrapy.Field()
    artistID = scrapy.Field()
    url = scrapy.Field()
    artistArea = scrapy.Field()
    artistStyle = scrapy.Field()
    artistStyleID = scrapy.Field()
    # artistDetail = scrapy.Field()
    # artistListen = scrapy.Field()
    artistFansNum = scrapy.Field()
    artistCommentNum = scrapy.Field()
    # artistLabel = scrapy.Field()
    # artistAlbumIDs = scrapy.Field()
    artistPict = scrapy.Field()


class XiamiAlbumItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    albumName = scrapy.Field()
    albumID = scrapy.Field()
    url = scrapy.Field()
    artistName = scrapy.Field()
    artistID = scrapy.Field()
    # albumLanguage = scrapy.Field()
    # albumCorp = scrapy.Field()
    albumDate = scrapy.Field()
    # albumType = scrapy.Field()
    # albumDetail = scrapy.Field()
    albumListen = scrapy.Field()
    albumFansNum = scrapy.Field()
    albumCommentNum = scrapy.Field()
    albumStar = scrapy.Field()
    # albumLabel = scrapy.Field()
    albumPict = scrapy.Field()
    albumSongID = scrapy.Field()
    albumSongName = scrapy.Field()

class XiamiSongItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    songName = scrapy.Field()
    songID = scrapy.Field()
    url = scrapy.Field()
    songLyric = scrapy.Field()
    songAlbum = scrapy.Field()
    songAlbumID = scrapy.Field()
    songSinger = scrapy.Field()
    songSingerID = scrapy.Field()
    songListen = scrapy.Field()
    songShareNum = scrapy.Field()
    songCommentNum = scrapy.Field()
    songRelated = scrapy.Field()
    songRelatedID = scrapy.Field()
    songRealID = scrapy.Field()

class XiamiMP3item(scrapy.Item):
    file_urls = scrapy.Field()
    songID = scrapy.Field()



