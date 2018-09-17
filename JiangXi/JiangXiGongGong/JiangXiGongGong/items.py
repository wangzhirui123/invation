# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JiangxigonggongItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    show_date = scrapy.Field()
    content = scrapy.Field()
    province_id = scrapy.Field()
    province = scrapy.Field()
    city = scrapy.Field()
    is_indb = scrapy.Field()
    url = scrapy.Field()
    county = scrapy.Field()
    city_id = scrapy.Field()
    county_id = scrapy.Field()
    sha1_url = scrapy.Field()