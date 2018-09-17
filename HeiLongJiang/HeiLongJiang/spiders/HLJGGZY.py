# -*- coding: utf-8 -*-

import scrapy
from urlparse import urljoin
from HeiLongJiang.items import HeilongjiangItem
from bs4 import BeautifulSoup
import hashlib
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class HljggzySpider(scrapy.Spider):
    name = 'HLJGGZY'
    class_type = '1'


    allowed_domains = ['http://www.hljggzyjyw.gov.cn/']
    start_urls = ['http://www.hljggzyjyw.gov.cn/trade/tradezfcg?cid=16']

    def parse(self, response):
        links = response.xpath('//div[@class="right_box"]/ul/li/a/@href')
        for i in links:
            yield scrapy.Request(urljoin('http://www.hljggzyjyw.gov.cn',i.extract()),callback=self.detail,dont_filter=True)

    def detail(self,response):
        items = HeilongjiangItem()
        items['url'] = response.url
        items['title'] = response.xpath('//div[@class="news_inf"]/h1/text()')[0].extract()
        items['content'] = str(BeautifulSoup(response.text).find_all('div',id="contentdiv")[0])
        items['show_date'] = str(response.xpath('//div[@class="nav-line"]/span/text()')[0].extract()).split('：')[-1].replace('年','-').replace('月','-').replace('日','')
        items['province'] = '黑龙江省'
        items['city'] = '0'
        items['county'] = '0'
        items['is_indb'] = '0'
        items['province_id'] = '230000'
        items['city_id'] = '0'
        items['county_id'] = '0'
        compile_url = hashlib.sha1(response.url)
        sha1_url = compile_url.hexdigest()
        items['sha1_url'] = sha1_url
        yield items









