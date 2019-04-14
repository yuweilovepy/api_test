# -*- coding:utf-8 -*-

import os

class FilePath:
    def __init__(self,dirname,filename=None):
        self.dirname=dirname
        self.filename=filename

    def dirpath(self):
        base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        dir_path=os.path.join(base_dir,self.dirname)
        return dir_path

    def filepath(self):
        file_path = os.path.join(self.dirpath(), self.filename)
        return file_path

if __name__ == '__main__':
    pth=FilePath("fools","log_pz.py").filepath()
    print(pth)