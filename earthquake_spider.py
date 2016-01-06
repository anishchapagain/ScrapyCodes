# -*- coding: utf-8 -*-
import scrapy
from earthquake.items import EarthquakeItem

#Nepal EarthQuake (Gorkha Apr-Dec 2015) and its Aftershocks.
#Data Scraped form http://www.seismonepal.gov.np
#anishchapagain@gmail.com

class EarthquakeSpiderSpider(scrapy.Spider):
    name = "earthquake_spider"
    allowed_domains = ["seismonepal.gov.np"]

	#Paging estimation for Roughly 5 Pages.
	#POST: {year:2015}
    start_urls = ['http://www.seismonepal.gov.np/index.php?action=earthquakes&show=past&year=2015&page=%s' % page for page in xrange(1,6)]
     
    def parse(self, response):
        print("Response Type >>> ",type(response)) #('Type >>> ', <class 'scrapy.http.response.html.HtmlResponse'>)
        rows = response.xpath("//div[@class='block2-content']//table[contains(.,'Date')]/tr") #correct    
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
