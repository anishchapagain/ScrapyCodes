# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EarthquakeItem(scrapy.Item):
    # define the fields for your item here like:
    edate = scrapy.Field()
    etime = scrapy.Field()
    elatitude = scrapy.Field()
    elongitude = scrapy.Field()
    emagnitude = scrapy.Field()
    epicentre = scrapy.Field()
    pass
