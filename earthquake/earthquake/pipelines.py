# -*- coding: utf-8 -*-
import re
from scrapy.exceptions import DropItem
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class EarthquakePipeline(object):
    def process_item(self, item, spider):
#        if item['epicentre']=='':
#            raise DropItem("empty item found")
#        elif re.match('/Sind*/I',item['epicentre']):
#            item['epicentre']=re.sub('Sind*','Sindhupalchowk',item['epicentre'])
        return item
        


#        if item['id'] in self.ids_seen:
#            raise DropItem("Duplicate item found: %s" % item)
#        else:
#            self.ids_seen.add(item['id'])
#            return item

# if item['price']:
#            if item['price_excludes_vat']:
#                item['price'] = item['price'] * self.vat_factor
#            return item
#        else:
#            raise DropItem("Missing price in %s" % item)