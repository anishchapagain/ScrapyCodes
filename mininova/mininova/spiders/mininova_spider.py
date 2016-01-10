# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 12:51:30 2015

@author: anishchapagain
"""

from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors import LinkExtractor
from mininova.items import MininovaItem

class MininovaSpider(CrawlSpider):
    name='mininova'
    allowed_domains=['mininova.org']
    start_urls = ['http://www.mininova.org/yesterday']
    rules = [Rule(LinkExtractor(allow=['/tor/\d+']), 'parse_torrent')]

    def parse_torrent(self, response):
        torrent = MininovaItem()
        torrent['url'] = response.url
        torrent['name'] = response.xpath("//h1/text()").extract()
        torrent['description'] = response.xpath("//div[@id='description']").extract()
        torrent['size'] = response.xpath("//div[@id='info-left']/p[2]/text()[2]").extract()
        return torrent

