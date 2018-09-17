# -*- coding: utf-8 -*-
import scrapy
import urlparse
import sys
import re
reload(sys)
sys.setdefaultencoding('utf8')
class HebeijianshespiderSpider(scrapy.Spider):
    name = 'HeBeiJianSheSpider'
    allowed_domains = ['http://zbb.hebjs.gov.cn/hebgc2009/index.php?a=eng-anc-list']
    start_urls = ['http://zbb.hebjs.gov.cn/hebgc2009/index.php?a=eng-anc-list']

    def parse(self, response):
        links = response.xpath('//div[@id="fl_lt_div"]/table/tbody/tr/td/a/@href')
        for i in links:
            yield scrapy.Request(urlparse.urljoin('http://zbb.hebjs.gov.cn',i.extract()),callback=self.detail_parse,dont_filter=True)
            print i.extract()
            break

    def detail_parse(self,response):
        pro_num = str(response.xpath('//*[@id="second_body_right"]/table/tr[1]/td[2]/text()')[0].extract()).replace('\n','').replace(' ','')
        city = str(response.xpath('//*[@id="second_body_right"]/table/tr[1]/td[4]/text()')[0].extract()).replace('\n','').replace(' ','')
        pro_name = str(response.xpath('//*[@id="second_body_right"]/table/tr[2]/td[2]/span/text()')[0].extract()).replace('\n','').replace(' ','')
        construction_company = str(response.xpath('//*[@id="second_body_right"]/table/tr[3]/td[2]/text()')[0].extract()).replace('\n','').replace(' ','')
        pro_address = str(response.xpath('//*[@id="second_body_right"]/table/tr[4]/td[2]/text()')[0].extract()).replace('\n','').replace(' ','')
        tender_phase = str(response.xpath('//*[@id="second_body_right"]/table/tr[5]/td[4]/text()')[0].extract()).replace('\n','').replace(' ','')
        business_area = ''
        pro_nature = ''
        tr_obj = response.xpath('//*[@id="second_body_right"]/table/tr')[-1]
        content = str(tr_obj.xpath('td[2]')[0].xpath('string(.)')[0].extract()).replace(' ','')
        c = re.findall('(2\.项目概况与招标范围(.*?)3\.投标人资格要求)',content,re.S)[0][0].split('\n                ')
        print content
        pro_desc = ''
        for i in c[1:-1]:
            srt_info = re.compile('^[1-9]\d*\.[1-9]\d*')
            new_cool = srt_info.sub('',i).replace('.','').replace('招标','项目')
            pro_desc+= new_cool+','

        # link = response.url
        # contact_man = str(response.xpath('//*[@id="second_body_right"]/table/tr[13]/td[2]/text()')[0].extract()).replace('\n','').replace(' ','')
        # # contact_phone = scrapy.Field()
        print '1'*30,unicode(pro_desc).encode('utf8')




