#- *- coding:utf-8 -*-


#  使用正则表达式进行数据的处理
import re
from common.path_file import FilePath  # 获取路径
from config.peizhi import DoPeiZhi    # 读取配置文件里的数据


t1_pth=FilePath("data","test1.ini").filepath()  #  获取t1的文件路径


# 查找 出来的value 作为 字典的key
s='"${a}","${b}"'
#data={"user_name":"lgh","pwd":12345}

# 写一个上下文管理器类
class Context:
    a=DoPeiZhi(t1_pth).get_strdata("data","a")
    b=DoPeiZhi(t1_pth).get_strdata("data","b")



#  根据python 反射进行动态加载属性
def new_replace(s):
    p="\$\{(.*?)}"
    while re.search(p,s):
        tmp=re.search(p,s).group(1)
        if hasattr(Context,tmp):
            value=getattr(Context,tmp)
            s=re.sub(p,value,s,count=1)
        else:
            return s
    return s


def replace(s,d):
    p = "\$\{(.*?)}"
    while re.search(p, s):
        tmp = re.search(p, s).group(1)
        value = str(d[tmp])
        s = re.sub(p, value, s, count=1)
    return s

#print(new_replace(s))