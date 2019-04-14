#- *- coding:utf-8 -*-

import hashlib

def getSign(user,password):
    str=user+password
    md5=hashlib.md5()
    md5.update(str.encode(encoding="utf-8"))
    sign=md5.hexdigest()
    return sign

print(getSign("lgh","123456"))