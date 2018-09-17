# -*- coding: utf-8 -*-
__author__ = 'Px'

import sys
import MySQLdb
import xlwt
reload(sys)
sys.setdefaultencoding('utf8')

def Get_user(user_id):
    sql_sele = 'select realname from user where id = %d'%user_id
    try:
        cur.execute(sql_sele)
        return cur.fetchone()[0]
    except:
        return 'XXX'



def Getdata():

    sql_sele = 'select * from commute where project_id=140'
    cur.execute(sql_sele)
    data = cur.fetchall()

    for i in data:
        # print i[1]
        if Get_user(i[1]) == 'XXX':
            continue
        with open('aaa.txt','a+')as f:
            f.write(Get_user(i[1])+':'+str(i[3])+' - '+str(i[5])+'\n')

if __name__ == '__main__':
    conn = MySQLdb.connect('59.110.165.161','root','Myjr678!@#','ygxt',charset='utf8')
    cur = conn.cursor()
    wb = xlwt.Workbook()
    sheet = wb.add_sheet('sheet1')
    Getdata()
