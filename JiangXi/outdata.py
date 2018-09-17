# -*- coding: utf-8 -*-
__author__ = 'Px'

import sys
import re
import time
import requests
import MySQLdb
import random
import pymongo
from lxml import etree
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf8')

def OutData():
    data = MongoTB.find({'province_name':'江西省1'})
    a = 0
    for i in data:
        try:
            operation_subscribeCount = random.randint(10,20)
            operation_bidcount = random.randint(10,20)
            # sql_in = 'insert into bid_invitation(title,province_id,province_name,publish_time,detail_html,source_link,iscatch,operation_subscribeCount,operation_bidcount,review_status)VALUE ("%s","%d","%s","%s","%s","%s","%d","%d","%d","%d")'%(i['title'],int(i['province_id']),i['province_name'],i['publish_time'],i['content'].replace('"','\''),"#",1,operation_subscribeCount,operation_bidcount,2)
            sql_in1 = 'insert into bid_winbid (title,province_id,province_name,publish_time,detail_html,source_link,iscatch)VALUES ("%s","%d","%s","%s","%s","%s","%d")'%(i['title'],int(i['province_id']),i['province_name'],i['publish_time'],i['content'].replace('"','\''),"#",1)

            cur.execute(sql_in1)
            conn.commit()
            a+=1
            print a
        except:
            continue


if __name__ == '__main__':
    conn = MySQLdb.connect('101.201.70.139','root','Myjr678!@#','ant',charset='utf8')
    cur = conn.cursor()
    MongoClient = pymongo.MongoClient()
    MongoDB = MongoClient['JX']
    MongoTB = MongoDB['JXTB']

    OutData()
