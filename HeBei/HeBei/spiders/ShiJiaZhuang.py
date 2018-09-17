# -*- coding: utf-8 -*-
import scrapy
import json
import hashlib
import MySQLdb
from urlparse import urljoin
from bs4 import BeautifulSoup
from HeBei.items import HebeiItem

conn = MySQLdb.Connect('101.201.70.139','root','Myjr678!@#','ant',charset='utf8')
cur = conn.cursor()
class HebeiggzySpider(scrapy.Spider):

    name = 'ShiJiaZhuang'
    class_type = "1"

    def start_requests(self):
        url = 'http://www.hebpr.cn/inteligentsearch/rest/inteligentSearch/getFullTextDataNew'
        dict_data = {
            "省本级":{"token":"","pn":0,"rn":10,"sdt":"","edt":"","wd":"","inc_wd":"","exc_wd":"","fields":"title","cnum":"001","sort":"{\"showdate\":\"0\"}","ssort":"title","cl":200,"terminal":"","condition":[{"fieldName":"categorynum","isLike":'true',"likeType":2,"equal":"003005"},{"fieldName":"infoc","isLike":'true',"likeType":2,"equal":"1300"}],"time":'null',"highlights":"title","statistics":'null',"unionCondition":'null',"accuracy":"","noParticiple":"0","searchRange":'null',"isBusiness":1},
            "石家庄市":{"token":"","pn":0,"rn":10,"sdt":"","edt":"","wd":"","inc_wd":"","exc_wd":"","fields":"title","cnum":"001","sort":"{\"showdate\":\"0\"}","ssort":"title","cl":200,"terminal":"","condition":[{"fieldName":"categorynum","isLike":"true","likeType":2,"equal":"003005"},{"fieldName":"infoc","isLike":"true","likeType":2,"equal":"1301"}],"time":"null","highlights":"title","statistics":"null","unionCondition":"null","accuracy":"","noParticiple":"0","searchRange":"null","isBusiness":1},
            "承德市":{"token":"","pn":0,"rn":10,"sdt":"","edt":"","wd":"","inc_wd":"","exc_wd":"","fields":"title","cnum":"001","sort":"{\"showdate\":\"0\"}","ssort":"title","cl":200,"terminal":"","condition":[{"fieldName":"categorynum","isLike":"true","likeType":2,"equal":"003005"},{"fieldName":"infoc","isLike":"true","likeType":2,"equal":"1308"}],"time":"null","highlights":"title","statistics":"null","unionCondition":"null","accuracy":"","noParticiple":"0","searchRange":"null","isBusiness":1},
            "张家口市":{"token":"","pn":0,"rn":10,"sdt":"","edt":"","wd":"","inc_wd":"","exc_wd":"","fields":"title","cnum":"001","sort":"{\"showdate\":\"0\"}","ssort":"title","cl":200,"terminal":"","condition":[{"fieldName":"categorynum","isLike":"true","likeType":2,"equal":"003005"},{"fieldName":"infoc","isLike":"true","likeType":2,"equal":"1307"}],"time":"null","highlights":"title","statistics":"null","unionCondition":"null","accuracy":"","noParticiple":"0","searchRange":"null","isBusiness":1},
            "秦皇岛市":{"token":"","pn":0,"rn":10,"sdt":"","edt":"","wd":"","inc_wd":"","exc_wd":"","fields":"title","cnum":"001","sort":"{\"showdate\":\"0\"}","ssort":"title","cl":200,"terminal":"","condition":[{"fieldName":"categorynum","isLike":"true","likeType":2,"equal":"003005"},{"fieldName":"infoc","isLike":"true","likeType":2,"equal":"1303"}],"time":"null","highlights":"title","statistics":"null","unionCondition":"null","accuracy":"","noParticiple":"0","searchRange":"null","isBusiness":1},
            "唐山市":{"token":"","pn":0,"rn":10,"sdt":"","edt":"","wd":"","inc_wd":"","exc_wd":"","fields":"title","cnum":"001","sort":"{\"showdate\":\"0\"}","ssort":"title","cl":200,"terminal":"","condition":[{"fieldName":"categorynum","isLike":"true","likeType":2,"equal":"003005"},{"fieldName":"infoc","isLike":"true","likeType":2,"equal":"1302"}],"time":"null","highlights":"title","statistics":"null","unionCondition":"null","accuracy":"","noParticiple":"0","searchRange":"null","isBusiness":1},
            "廊坊市":{"token":"","pn":0,"rn":10,"sdt":"","edt":"","wd":"","inc_wd":"","exc_wd":"","fields":"title","cnum":"001","sort":"{\"showdate\":\"0\"}","ssort":"title","cl":200,"terminal":"","condition":[{"fieldName":"categorynum","isLike":"true","likeType":2,"equal":"003005"},{"fieldName":"infoc","isLike":"true","likeType":2,"equal":"1310"}],"time":"null","highlights":"title","statistics":"null","unionCondition":"null","accuracy":"","noParticiple":"0","searchRange":"null","isBusiness":1},
            "保定市":{"token":"","pn":0,"rn":10,"sdt":"","edt":"","wd":"","inc_wd":"","exc_wd":"","fields":"title","cnum":"001","sort":"{\"showdate\":\"0\"}","ssort":"title","cl":200,"terminal":"","condition":[{"fieldName":"categorynum","isLike":"true","likeType":2,"equal":"003005"},{"fieldName":"infoc","isLike":"true","likeType":2,"equal":"1306"}],"time":"null","highlights":"title","statistics":"null","unionCondition":"null","accuracy":"","noParticiple":"0","searchRange":"null","isBusiness":1},
            "沧州市":{"token":"","pn":0,"rn":10,"sdt":"","edt":"","wd":"","inc_wd":"","exc_wd":"","fields":"title","cnum":"001","sort":"{\"showdate\":\"0\"}","ssort":"title","cl":200,"terminal":"","condition":[{"fieldName":"categorynum","isLike":"true","likeType":2,"equal":"003005"},{"fieldName":"infoc","isLike":"true","likeType":2,"equal":"1309"}],"time":"null","highlights":"title","statistics":"null","unionCondition":"null","accuracy":"","noParticiple":"0","searchRange":"null","isBusiness":1},
            "衡水市":{"token":"","pn":0,"rn":10,"sdt":"","edt":"","wd":"","inc_wd":"","exc_wd":"","fields":"title","cnum":"001","sort":"{\"showdate\":\"0\"}","ssort":"title","cl":200,"terminal":"","condition":[{"fieldName":"categorynum","isLike":"true","likeType":2,"equal":"003005"},{"fieldName":"infoc","isLike":"true","likeType":2,"equal":"1311"}],"time":"null","highlights":"title","statistics":"null","unionCondition":"null","accuracy":"","noParticiple":"0","searchRange":"null","isBusiness":1},
            "邢台市":{"token":"","pn":0,"rn":10,"sdt":"","edt":"","wd":"","inc_wd":"","exc_wd":"","fields":"title","cnum":"001","sort":"{\"showdate\":\"0\"}","ssort":"title","cl":200,"terminal":"","condition":[{"fieldName":"categorynum","isLike":"true","likeType":2,"equal":"003005"},{"fieldName":"infoc","isLike":"true","likeType":2,"equal":"1305"}],"time":"null","highlights":"title","statistics":"null","unionCondition":"null","accuracy":"","noParticiple":"0","searchRange":"null","isBusiness":1},
            "邯郸市":{"token":"","pn":0,"rn":10,"sdt":"","edt":"","wd":"","inc_wd":"","exc_wd":"","fields":"title","cnum":"001","sort":"{\"showdate\":\"0\"}","ssort":"title","cl":200,"terminal":"","condition":[{"fieldName":"categorynum","isLike":"true","likeType":2,"equal":"003005"},{"fieldName":"infoc","isLike":"true","likeType":2,"equal":"1304"}],"time":"null","highlights":"title","statistics":"null","unionCondition":"null","accuracy":"","noParticiple":"0","searchRange":"null","isBusiness":1},
            "定州市":{"token":"","pn":0,"rn":10,"sdt":"","edt":"","wd":"","inc_wd":"","exc_wd":"","fields":"title","cnum":"001","sort":"{\"showdate\":\"0\"}","ssort":"title","cl":200,"terminal":"","condition":[{"fieldName":"categorynum","isLike":"true","likeType":2,"equal":"003005"},{"fieldName":"infoc","isLike":"true","likeType":2,"equal":"139001"}],"time":"null","highlights":"title","statistics":"null","unionCondition":"null","accuracy":"","noParticiple":"0","searchRange":"null","isBusiness":1},
            "辛集市":{"token":"","pn":0,"rn":10,"sdt":"","edt":"","wd":"","inc_wd":"","exc_wd":"","fields":"title","cnum":"001","sort":"{\"showdate\":\"0\"}","ssort":"title","cl":200,"terminal":"","condition":[{"fieldName":"categorynum","isLike":"true","likeType":2,"equal":"003005"},{"fieldName":"infoc","isLike":"true","likeType":2,"equal":"139002"}],"time":"null","highlights":"title","statistics":"null","unionCondition":"null","accuracy":"","noParticiple":"0","searchRange":"null","isBusiness":1} }

        for i in dict_data:
            yield scrapy.Request(url=url,method="POST",body=json.dumps(dict_data[i]),meta={'city':i})

    def parse(self, response):

        data = json.loads(response.text)['result']['records']
        for i in data:

            yield scrapy.Request(urljoin('http://www.hebpr.cn/',i['linkurl']),callback=self.detail,meta={'title':i['title'],'showdate':i['showdate'],"is_indb":"0","city":response.meta['city'],"county":i['zhuanzai']})




    def GetCountyId(self,name):

        sql_sele = "select Id from county where county_name ='%s'"%name
        cur.execute(sql_sele)
        try:
            Id = cur.fetchone()[0]
            return Id
        except:
            return 0

    def GetCityId(self,name):
        sql_sele = 'select Id from city where city_name="%s"'%name
        cur.execute(sql_sele)
        try:
            Id = cur.fetchone()[0]
            return Id
        except:
            return 0



    def detail(self,response):
        items = HebeiItem()
        html_obj = BeautifulSoup(response.text)
        items['content'] = str(html_obj.find_all('div',class_="ewb-comp-bd")[0])
        items['url'] = response.url
        items['title'] = response.meta['title']
        items['show_date'] = response.meta['showdate']
        items['province'] = "河北省"
        items['city'] = response.meta['city']
        items['county'] = response.meta['county']
        items['is_indb'] = "0"
        items['province_id'] = "130000"
        items['city_id'] = str(self.GetCityId(response.meta['city']))
        items['county_id'] = str(self.GetCountyId(response.meta['county']))
        compile_url = hashlib.sha1(response.url)
        sha1_url = compile_url.hexdigest()
        items['sha1_url'] = sha1_url
        yield items












