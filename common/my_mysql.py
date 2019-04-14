# -*- coding:utf-8 -*-

import pymysql

class Mysql:
    def __init__(self,return_dict=False):
        self.mysql = pymysql.connect(host="localhost", user="root", password="123456", database="book")
        # print(mysql)
        if return_dict:
            self.cursor=self.mysql.cursor(pymysql.cursors.DictCursor)  #  返回字典
        else:
            self.cursor = self.mysql.cursor()


    def fetch_one(self,sql):
        self.cursor.execute(sql)
        result=self.cursor.fetchone()
        return result


    def mysql_close(self):
        self.cursor.close()
        self.mysql.close()


if __name__ == '__main__':
    cursor=Mysql()
    result=cursor.fetch_one("select * from emp")
    cursor.mysql_close()
    print(result)