# -*- coding: utf-8 -*-
import scrapy
import json

class JilinzhaobiaoSpider(scrapy.Spider):
    name = 'JiLinZhaoBiao'
    allowed_domains = ['http://was.jl.gov.cn']
    start_urls = ['http://was.jl.gov.cn/was5/web/search?channelid=237687&page=1&prepage=17&searchword=gtitle%3C%3E%27%27%20and%20gtitle%3C%3E%27null%27%20and%20tType=%27%E6%94%BF%E5%BA%9C%E9%87%87%E8%B4%AD%27%20and%20iType=%27%E9%87%87%E8%B4%AD%E5%85%AC%E5%91%8A%27%20&callback&callback=result']

    def parse(self, response):
        print json.loads(response.text)
        # for i in dict_data['datas']:
        #     print i

