#- *- coding:utf-8 -*-

from configparser import ConfigParser


class DoPeiZhi:
    def __init__(self,filename):
        self.config=ConfigParser()
        self.config.read(filename,encoding="utf-8")


    def get_strdata(self,section,value):
        return self.config.get(section,value)


    def get_floatdata(self,section,value):
        return self.config.getfloat(section,value)

    def get_booldata(self,section,value):
        return self.config.getboolean(section,value)

    def get_intdata(self,section,value):
        return self.config.getint(section,value)

    def get_dictorlist_data(self,section,value):
        return eval(self.config.get(section,value))

if __name__ == '__main__':
    res=DoPeiZhi("../data/config.ini").get_dictorlist_data("message","t5")
    print(res,type(res))

