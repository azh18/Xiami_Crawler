# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from Xiami_test.items import *
from string import atoi
from time import sleep


def ToJsonStr(str1):
    return str1.replace('\"', '\\\"').replace('\\', '\\\\').replace('/', '\\/').replace('\b', ' ').replace('\f', ' ') \
        .replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')

class XiaMiSpider(CrawlSpider):
    name = 'xiamiSpider'
    allowed_domains = ['xiami.com']
    start_urls = []
    for i in xrange(1, 416):
        start_urls.append('http://www.xiami.com/artist/index/c/2/type/0/class/0/page/' + str(i))

    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        Rule(LinkExtractor(allow=('/artist/[a-zA-Z0-9]{0,11}$', )), callback='parse_artist'),
        Rule(LinkExtractor(allow=('/album/[a-zA-Z0-9]{0,11}$',)), callback='parse_album'),
        Rule(LinkExtractor(allow=('/song/[a-zA-Z0-9]{0,11}$',)), callback='parse_song')

        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        # Rule(LinkExtractor(allow=('item\.php', )), callback='parse_item'),
    )



    def parse_artist(self, response):
        item = XiamiArtistItem()
        sleep(2)
        # two kinds of pages of artists
        if not (len(response.xpath(u"//*[@id='title']/h1/text()").extract())): # i.xiami.com
            if len(response.xpath(u"//*[@id='glory-title']/div/div/h1/text()").extract()) == 0:
                sleep(60*5)

            # artist information
            area = response.xpath(u"// *[ @ id = 'artist_info'] // table // tr["
                                  u"contains(td[1]/text(),'地区')]/td[2]/text()").extract()
            item['artistArea'] = list()
            for i in area:
                item['artistArea'].append(ToJsonStr(i))
            # detail = response.xpath(u"// *[ @ id = 'artist_info'] // table // "
            #                                   u"tr[contains(td[1]/text(),'档案')]/td[2]/div/text()").extract()
            # item['artistDetail'] = "\n".join(detail)

            artist = response.xpath(u"//*[@id='glory-title']/div/div/h1/text()").extract()
            item['artistName'] = list()
            for i in artist:
                item['artistName'].append(ToJsonStr(i))

            item['url'] = response.meta['redirect_urls'][0]
            item['artistID'] = item['url'].split('/')[-1]
            # Style
            style = response.xpath(u"// *[ @ id = 'artist_info'] // table // tr"
                                                 u"[contains(td[1]/text(),'风格')]/td[2]/a/text()").extract()
            styleLink = response.xpath(u"// *[ @ id = 'artist_info'] // table // tr[contains(td[1]/te"
                                                   u"xt(),'风格')]/td[2]/a/@href").extract()
            # if there is no style data, don't process
            if len(style):
                styles = list()
                for i in style:
                    styles.append(ToJsonStr(i.split('/')[-1]))
                item['artistStyle'] = styles
            if len(styleLink):
                styles = list()
                for i in styleLink:
                    styles.append(ToJsonStr(i.split('/')[-1]))
                item['artistStyleID'] = styles
            # fans number and comment number
            fans = response.xpath("//*[@id='sidebar']/div[1]/ul/li[2]/a/text()").extract()
            if len(fans):
                fans = fans[0]
                item['artistFansNum'] = atoi(fans)
            comment = response.xpath("//*[@id='sidebar']/div[1]/ul/li[3]/a/text()").extract()
            if len(comment):
                comment = comment[0]
                item['artistCommentNum'] = atoi(comment)
            # artist picture
            pictureURL = response.xpath("//*[@id='cover_lightbox']/@href").extract()
            if len(pictureURL):
                item['artistPict'] = pictureURL[0]

            albumURL = u"http://www.xiami.com" + "".join(response.xpath(u"//*[@id='nav']/a[3]/@href").extract())

        else:
            if len(response.xpath(u"//*[@id='title']/h1/text()").extract()) == 0:
                sleep(60*5)
            area = response.xpath(u"// *[ @ id = 'artist_info'] // table // tr["
                                                u"contains(td[1]/text(),'地区')]/td[2]/text()").extract()
            item['artistArea'] =list()
            for i in area:
                item['artistArea'].append(ToJsonStr(i))
            # detail = response.xpath(u"// *[ @ id = 'artist_info'] // table // "
            #                                   u"tr[contains(td[1]/text(),'档案')]/td[2]/div/text()").extract()
            # item['artistDetail'] = "\n".join(detail)

            artist = response.xpath(u"//*[@id='title']/h1/text()").extract()
            item['artistName'] = list()
            for i in artist:
                item['artistName'].append(ToJsonStr(i))

            item['url'] = response.url
            item['artistID'] = item['url'].split('/')[-1]
            # Style
            style = response.xpath(u"// *[ @ id = 'artist_info'] // table // tr"
                                                 u"[contains(td[1]/text(),'风格')]/td[2]/a/text()").extract()
            styleLink = response.xpath(u"// *[ @ id = 'artist_info'] // table // tr[contains(td[1]/te"
                                                   u"xt(),'风格')]/td[2]/a/@href").extract()
            # if there is no style data, don't process
            if len(style):
                styles = list()
                for i in style:
                    styles.append(ToJsonStr(i.split('/')[-1]))
                item['artistStyle'] = styles
            if len(styleLink):
                styles = list()
                for i in styleLink:
                    styles.append(ToJsonStr(i.split('/')[-1]))
                item['artistStyleID'] = styles
            # fans number and comment number
            fans = response.xpath("//*[@id='sidebar']/div[1]/ul/li[2]/a/text()").extract()
            if len(fans):
                fans = fans[0]
                item['artistFansNum'] = atoi(fans)
            comment = response.xpath("//*[@id='sidebar']/div[1]/ul/li[3]/a/text()").extract()
            if len(comment):
                comment = comment[0]
                item['artistCommentNum'] = atoi(comment)
            # artist picture
            pictureURL = response.xpath("//*[@id='cover_lightbox']/@href").extract()
            if len(pictureURL):
                item['artistPict'] = pictureURL[0]

            albumURL = u"http://www.xiami.com" + "".join(response.xpath(u"//*[@id='nav']/a[3]/@href").extract())
        yield scrapy.Request(albumURL)
        yield item

    def parse_album(self, response):
        sleep(2)
        item = XiamiAlbumItem()
        ss = response.xpath(
                u"//*[@id='album_info']/table//tr[contains(td[1]/text(),'艺人')]/td[2]/a/text()").extract()
        if len(ss)==0:
            sleep(60*5)
        item['artistName'] = list()
        artists = response.xpath(u"//*[@id='album_info']/table//tr[contains(td[1]/text(),'艺人')]/td[2]/a/text()").extract()
        for i in artists:
            item['artistName'].append(ToJsonStr(i))

        albums = response.xpath('//*[@id="title"]/h1/text()').extract()[0]
        item['albumName'] = ToJsonStr(albums)

        item['url'] = response.url
        item['albumID'] = item['url'].split('/')[-1]
        artistURL = response.xpath('//*[@id="album_info"]/table//a[contains(@href,"artist")]/@href').extract()[0]
        item['artistID'] = artistURL.split('/')[-1]

        albumDate = response.xpath(u"//*[@id='album_info']/table//tr[contains(td[1]/text(),'发行时间')]/td[2]/text()").extract()
        if len(albumDate):
            item['albumDate'] = albumDate
        listenNum = response.xpath(u"//*[@id='sidebar']/div[1]/ul/li[contains(span/text(),'试听')]/text()").extract()
        if len(listenNum):
            item['albumListen'] = listenNum[0]
        albumFansNum = response.xpath(u"//*[@id='sidebar']/div[1]/ul/li[contains(span/text(),'收藏')]/text()").extract()
        if len(albumFansNum):
            item['albumFansNum'] = albumFansNum[0]
        albumCommentNum = response.xpath(u"//*[@id='sidebar']/div[1]/ul/li[contains(a/span/text(),'评论')]/a/i/text()").extract()
        if len(albumCommentNum):
            item['albumCommentNum'] = albumCommentNum[0]
        star = response.xpath(u"//*[@id='album_rank']/p/em/text()").extract()
        if len(star):
            item['albumStar'] = star[0]
        albumPictURL = response.xpath(u"//*[@id='cover_lightbox']/@href").extract()
        if len(albumPictURL):
            item['albumPict'] = albumPictURL[0]
        songURL = response.xpath(u"//*[@id='track']//tr//td[@class='song_name']/a[contains(@href,'song')]/@href").extract()
        if len(songURL):
            for elem in songURL:
                elem = u"http://www.xiami.com" + elem
                yield scrapy.Request(elem)
        songURL = response.xpath(u"//*[@id='track']//tr//td[@class='song_name']/a[contains(@href,'song')]/@href").extract()
        if len(songURL):
            item['albumSongID'] = []
            for elem in songURL:
                item['albumSongID'].append(elem.split('/')[-1])

        songNames = response.xpath(u"//*[@id='track']//tr//td[@class='song_name']/a[contains(@href,'song')]/text()").extract()
        item['albumSongName'] = list()
        for i in songNames:
            item['albumSongName'].append(ToJsonStr(i))
        yield item


    def parse_song(self, response):
        sleep(2)
        item = XiamiSongItem()
        if len(response.xpath(u"//*[@id='title']/h1/text()").extract()) == 0:
            sleep(60*5)

        songs = response.xpath(u"//*[@id='title']/h1/text()").extract()[0]
        item['songName'] = ToJsonStr(songs)

        item['url'] = response.url
        item['songID'] = item['url'].split('/')[-1]
        # lyric process
        lyrics = response.xpath(u"//*[@id='lrc']/div[contains(@class,'main')]/text()").extract()
        str1 = ""
        for i in lyrics:
            str1 = str1 + ' ' + ToJsonStr(i)
        item['songLyric'] = str1

        albums = response.xpath(u"//*[@id='albums_info']//tr//a[contains(@href,'album')]/text()").extract()
        if len(albums):
            item['songAlbum'] = ToJsonStr(albums[0])
        albumURL = response.xpath(u"//*[@id='albums_info']//tr//a[contains(@href,'album')]/@href").extract()
        if len(albumURL):
            item['songAlbumID'] = albumURL[0].split('/')[-1]
        # singers  may be many
        singers = response.xpath(u"//*[@id='albums_info']//tr//a[contains(@href,'artist')]/text()").extract()
        item['songSinger'] = list()
        for i in singers:
            item['songSinger'].append(ToJsonStr(i))

        item['songSingerID'] = list()
        artistURL = response.xpath(u"//*[@id='albums_info']//tr//a[contains(@href,'artist')]/@href").extract()
        for i in artistURL:
            str1 = i.split('/')[-1]
            item['songSingerID'].append(ToJsonStr(str1))

        # item['songListen']
        shareNum = response.xpath(u"//*[@id='sidebar']/div[1]/ul/li[contains(span/text(),'分享')]/text()").extract()
        if len(shareNum):
            item['songShareNum'] = shareNum[0]
        commentNum = response.xpath(u"//*[@id='sidebar']/div[1]/ul/li[contains(a/span/text(),'评论')]/a/text()").extract()
        if len(commentNum):
            item['songCommentNum'] = commentNum[0]
        # related songs

        songRelated = response.xpath(u"//*[@id='relate_song']//table//td[@class='song_name']/p/a[contains(@href,'song')]/t"
                                     u"ext()").extract()
        item['songRelated'] = list()
        for songName in songRelated:
            item['songRelated'].append(ToJsonStr(songName.split('\t')[1].split(' ')[0]))

        songRelatedIdList = response.xpath(u"//*[@id='relate_song']//table//td[@class='song_name']/p/a[contains(@href,"
                                           u"'song')]/@href").extract()
        if len(songRelatedIdList):
            item['songRelatedID'] = list()
            for songID in songRelatedIdList:
                item['songRelatedID'].append(songID.split('/')[-1])

        yield item