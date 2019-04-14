# -*- coding:utf-8 -*-
import os

real_path=os.path.realpath(__file__)
print("绝对路径",real_path)
pwd_path=os.getcwd()
print("当前目录",pwd_path)

print(os.listdir(pwd_path))  # 获取所有文件名 返回值是列表

for file in os.listdir(pwd_path):
    if os.path.isdir(file):
        print("{}是目录".format(file))
    elif os.path.isfile(file):
        print("{}是文件".format(file))
    else:
        pass

print(os.path.join(pwd_path,"kkk"))  #  拼接绝对路径
#  mkdir  rmdir  新建文件夹 删除文件夹

