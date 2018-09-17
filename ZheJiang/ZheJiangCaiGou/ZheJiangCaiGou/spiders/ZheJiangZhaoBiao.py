# -*- coding: utf-8 -*-
import scrapy
import sys
import re
import json
import time
import hashlib
reload(sys)
sys.setdefaultencoding('utf8')
from ZheJiangCaiGou.items import ZhejiangcaigouItem



class ZhejiangzhaobiaoSpider(scrapy.Spider):
    class_type = '1'
    name = 'ZheJiangZhaoBiao'
    allowed_domains = ['http://manager.zjzfcg.gov.cn']
    start_urls = ['http://manager.zjzfcg.gov.cn/cms/api/cors/getRemoteResults?pageSize=15&pageNo=1&noticeType=10&url=http%3A%2F%2Fnotice.zcy.gov.cn%2Fnew%2FnoticeSearch']

    def parse(self, response):
        dict_data = json.loads(response.text.encode('utf8'))
        items = dict_data['articles']
        for i in items:
            title = i['title']

            url = 'http://manager.zjzfcg.gov.cn/cms/api/cors/getRemoteResults?noticeId={}&url=http%3A%2F%2Fnotice.zcy.gov.cn%2Fnew%2FnoticeDetail'.format(i['id'])
            yield scrapy.Request(url,callback=self.detailparse,dont_filter=True,meta={'title':title})

    def detailparse(self,response):
        items = ZhejiangcaigouItem()

        date = re.findall('"noticePubDate":"(.*?)",',response.text,re.S)[0].split()[0]
        content = re.findall('noticeContent":"(.*?)"\,"visitCount"',response.text,re.S)[0]
        items['title'] = response.meta['title']
        items['show_date'] = date
        items['content'] = content
        items['province_id'] = '330000'
        items['province'] = "浙江省"
        items['city'] = ''
        items['is_indb'] = '0'
        items['url'] = response.url
        items['county'] = ''
        items['city_id'] = '0'
        items['county_id'] = '0'
        compile_url = hashlib.sha1(response.url)
        sha1_url = compile_url.hexdigest()
        items['sha1_url'] = sha1_url
        yield items





