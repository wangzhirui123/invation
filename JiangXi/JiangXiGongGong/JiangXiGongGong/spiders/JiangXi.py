# -*- coding: utf-8 -*-
import scrapy
import urlparse
import hashlib
from bs4 import BeautifulSoup
from JiangXiGongGong.items import JiangxigonggongItem
class JiangxiSpider(scrapy.Spider):
    name = 'JiangXi'
    class_type = '1'
    allowed_domains = ['http://www.jxsggzy.cn']
    start_urls = ['http://www.jxsggzy.cn/web/jyxx/002006/002006001/jyxx.html']

    def parse(self, response):
        links = response.xpath('//div[@class="ewb-infolist"]/ul/li/a/@href')
        for u in links:
            yield scrapy.Request(urlparse.urljoin('http://www.jxsggzy.cn',u.extract()),callback=self.detail_parse,dont_filter=True)
        # next_page = response.xpath('//li[@class="nextlink"]/a[@class="alink"]/@href')[0].extract()
        # yield scrapy.Request(urlparse.urljoin('http://www.jxsggzy.cn',next_page),callback=self.parse,dont_filter=True)

    def detail_parse(self,response):
        items = JiangxigonggongItem()
        items['title'] = response.xpath('//h1/text()')[0].extract()
        items['show_date'] = response.xpath('//p[@class="infotime"]/text()')[0].extract().replace('\r\n            \t\t\t\t\t[','').replace(']','').replace('\r\n','')
        html_obj = BeautifulSoup(response.text)
        items['content'] = str(html_obj.find_all('div',class_="con")[0])
        items['province_id'] = 360000
        items['province'] = '江西省'
        items['is_indb'] = '0'
        items['url'] = response.url
        items['county'] = ''
        items['city_id'] = '0'
        items['county_id'] = '0'
        compile_url = hashlib.sha1(response.url)
        sha1_url = compile_url.hexdigest()
        items['sha1_url'] = sha1_url
        yield items






