# -*- coding: utf-8 -*-
import scrapy
import json
import MySQLdb
import hashlib
from urlparse import urljoin
from HeBei.items import HebeiItem
from bs4 import BeautifulSoup


conn = MySQLdb.connect('101.201.70.139','root','Myjr678!@#','ant',charset='utf8')
cur = conn.cursor()

class HebeizhengfucaigouSpider(scrapy.Spider):
    name = 'HeBeiZhengFuCaiGou'
    class_type ="2"


    def start_requests(self):

        yield scrapy.Request('http://search.hebcz.gov.cn:8080/was5/web/search?channelid=228483&province=130000000&city=&purchaseWay=&lanmu=zhbgg&syprovince=&sydoctitle=&admindivcode=130000000&purchaseWay1=&PurchaserName=&searchword1=',meta={"city":"省本级"})

    def parse(self, response):
        links = response.xpath('//tr[@id="biaoti"]/td[2]/a/@href')
        for u in links:
            yield scrapy.Request(u.extract()+'?1',callback=self.detail_parse,dont_filter=True,meta={'city':response.meta['city']})

    def GetCityId(self,name):
        sql_sele = 'select Id from city where city_name="%s"'%name
        cur.execute(sql_sele)
        try:
            Id = cur.fetchone()[0]
            return Id
        except:
            return 0


    def detail_parse(self,response):
        items = HebeiItem()
        items['content'] = response.xpath('//table[@width="1002"]/tr[4]/td')[0].extract().encode('utf8')
        items['url'] = response.url
        items['title'] = response.xpath('//span[@class="txt2"]/text()')[0].extract()
        items['show_date'] = response.xpath('//td[@class="txt7"]/span/text()')[0].extract()
        items['province'] = "河北省"
        items['city'] = response.meta['city']
        items['county'] = ""
        items['is_indb'] = "0"
        items['province_id'] = "130000"
        items['city_id'] = str(self.GetCityId(response.meta['city']))
        items['county_id'] = "0"
        compile_url = hashlib.sha1(response.url)
        sha1_url = compile_url.hexdigest()
        items['sha1_url'] = sha1_url
        yield items



