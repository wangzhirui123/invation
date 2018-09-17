#encoding:utf8

import pymongo
import MySQLdb
import random
import redis
def GetMongoData():
    MyQuery = Mongo_Tab.find({'is_indb':"0"})
    if MyQuery.count() > 0:
        return MyQuery
    else:
        return []

def Update_MongoData(sha1_data):
    MyQuery = {"title":sha1_data}
    NewValue = {"$set":{"is_indb":"1"}}
    Mongo_Tab.update(MyQuery,NewValue)


def InMySQL(set_data):
    if set_data.count() >0:
        print set_data.count()
        for i in set_data:
            print '111111111111'
            operation_subscribeCount = random.randint(10,20)
            operation_bidcount = random.randint(10,20)
            try:
                sql_in = 'insert into bid_invitation(title,province_id,province_name,city_id,city_name,county_id,county_name,publish_time,detail_html,source_link,iscatch,operation_subscribeCount,operation_bidcount,review_status)VALUE ("%s","%d","%s","%d","%s","%d","%s","%s","%s","%s","%d","%d","%d","%d")'%(i['title'],int(i['province_id']),i['province'],int(i['city_id']),i['city'],int(i['county_id']),i['county'],i['show_date'],i['content'].replace('"','\'').replace("<div id='hideDeil' style='display:none'>",''),i['url'],1,operation_subscribeCount,operation_bidcount,2)

                sql_in1 = 'insert into bid_winbid (title,province_id,province_name,city_id,city_name,county_id,county_name,publish_time,detail_html,source_link,iscatch)VALUES ("%s","%d","%s","%d","%s","%d","%s","%s","%s","%s","%d")'%(i['title'],int(i['province_id']),i['province'],int(i['city_id']),i['city'],int(i['county_id']),i['county'],i['show_date'],i['content'].replace('"','\'').replace("<div id='hideDeil' style='display:none'>",''),i['url'],1)
                MySQL_Cur.execute(sql_in)
                MySQL_Client.commit()

                # Redis_Client.lpush('index_zhaobiaolist','{"id":%s,"title":"%s","publish_time":"%s"}'%(str(MySQL_Cur.lastrowid),i['title'],i['show_date']))
                # Redis_Client.client_kill('39.105.11.191')
            except:
                continue
            Update_MongoData(i['title'])
    else:
        print '没有新的数据'

def update_data():
    sql_sele = 'select id,detail_html from bid_invitation where province_id = 130000 limit 3000'
    MySQL_Cur.execute(sql_sele)
    data = MySQL_Cur.fetchall()
    for i in data:
        detail_html = i[1].replace("<div id='hideDeil' style='display:none'>",'').replace('id','').replace("'","\"")
        # print detail_html
        sql_update = "update bid_invitation set detail_html='%s' where id =%d"%(detail_html,i[0])
        MySQL_Cur.execute(sql_update)
        MySQL_Client.commit()

if __name__ == '__main__':
    Mongo_Client = pymongo.MongoClient()
    Redis_Client = redis.Redis('39.105.11.191',port=6379,password='123')
    Mongo_DB = Mongo_Client['HeBei']
    Mongo_Tab = Mongo_DB['invitation']
    MySQL_Client = MySQLdb.connect('101.201.70.139','root','Myjr678!@#','ant',charset='utf8')
    MySQL_Cur = MySQL_Client.cursor()
    InMySQL(GetMongoData())
    # update_data()
