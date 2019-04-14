#- *- coding:utf-8 -*-

import yaml

class Doyaml:
    def __init__(self,filename):
        self.f=open(filename)
        self.data=yaml.load(self.f)

    def get_data(self,item1,item2=None):
        for key,value in self.data.items():
            #print(key,value)
            pass


if __name__ == '__main__':
    res=Doyaml("../data/file.yaml").get_data("name")


