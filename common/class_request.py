# -*- coding:utf-8 -*-

import requests
import json
from fools.log_pz import Log

class Requests:
    def __init__(self):
        self.session=requests.session()
        self.log=Log("request")

    def request(self,method,url,data=None):
        self.log.info("这是一个测试")
        method=method.upper()
        if data is not None and isinstance(data,str):
            data=json.loads(data)
        else:
            pass
        if method=="GET":
            response=self.session.get(url,params=data)
            message=response.url
        elif method=="POST":
            response=self.session.post(url,data=data)
            message=response.url
        else:
            return ("MESSAGE IS ERROR")
        return message

if __name__ == '__main__':
    data={"name":"lgh","age":"28","job":"no"}
    res=Requests()
    #print(res.request("get","http://postman-echo.com/get",data))
    print(res.request("post","http://postman-echo.com/post",data))