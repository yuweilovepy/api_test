# -*- coding:utf-8 -*-

from config.peizhi import DoPeiZhi
from common.path_file import FilePath
from common.class_request import Requests

g_pth=FilePath("data","gloable.ini").filepath()
t1_pth=FilePath("data","test1.ini").filepath()
t2_pth=FilePath("data","test2.ini").filepath()


def peizhi_data():
    res=DoPeiZhi(g_pth).get_booldata("env","switch")
    if res:
        url=DoPeiZhi(t1_pth).get_strdata("api","url")
    else:
        url=DoPeiZhi(t2_pth).get_strdata("api","url")
    return url

res=Requests()
response=res.request("get",peizhi_data())
print(response)