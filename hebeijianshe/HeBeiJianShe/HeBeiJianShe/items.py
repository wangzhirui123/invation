# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HebeijiansheItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pro_num = scrapy.Field()
    city = scrapy.Field()
    pro_name = scrapy.Field()
    construction_company = scrapy.Field()
    pro_address = scrapy.Field()
    tender_phase = scrapy.Field()
    business_area = scrapy.Field()
    pro_nature = scrapy.Field()
    pro_desc = scrapy.Field()
    link = scrapy.Field()
    contact_man = scrapy.Field()
    contact_phone = scrapy.Field()

