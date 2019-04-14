# -*- coding:utf-8 -*-

from urllib import parse

data={"city":"北京"}

city=parse.urlencode(data).encode("utf-8")  # 中文进行编码
print(city)