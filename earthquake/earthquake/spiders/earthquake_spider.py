# -*- coding: utf-8 -*-
import scrapy
from earthquake.items import EarthquakeItem

#Nepal EarthQuake Related Data for Year 2015.
#Data Scraped from http://www.seismonepal.gov.np
#anishchapagain@gmail.com

class EarthquakeSpiderSpider(scrapy.Spider)
    name = "earthquake_spider"
    allowed_domains = ["seismonepal.gov.np"]

#Paging estimation for Roughly 5 Pages.
#POST: {year:2015}
    def start_requests(self):
        for page in xrange(1,6):
            url='http://www.seismonepal.gov.np/index.php?action=earthquakes&show=past&page=%s' % page
            print("Procsessing Page ",url)
            yield scrapy.FormRequest(url,formdata={'year': '2015'},callback=self.parse)

    def parse(self, response):
        print("Response Type >>> ",type(response)) 
        rows = response.xpath("//div[@class='block2-content']//table[contains(.,'Date')]/tr") 
        print("count >> ",rows.__len__())
        
        for row in rows:
            item = EarthquakeItem()
            item['edate']=row.xpath('td[1]/span/text()').extract()
            item['etime']=row.xpath('td[2]/span/text()').extract()
            item['elatitude']=row.xpath('td[3]/span/text()').extract()
            item['elongitude']=row.xpath('td[4]/span/text()').extract()
            item['emagnitude']=row.xpath('td[5]/span/text()').extract()
            item['epicentre']=row.xpath('td[6]/span/a/text()').extract()
            yield item
        
        print('Completed')   
