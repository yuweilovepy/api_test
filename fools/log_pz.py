# -*- coding:utf-8 -*-

import logging, time, os
from common.path_file import FilePath
from config.peizhi import DoPeiZhi  # 读取配置文件里的数据

# 使用RotatingFileHandler，可以实现日志回滚，

g_pth = FilePath("data", "gloable.ini").filepath()
t1_pth = FilePath("data", "test1.ini").filepath()
t2_pth = FilePath("data", "test2.ini").filepath()
res = DoPeiZhi(g_pth).get_booldata("env", "switch")

# 日志保存本地的地址 可配置

log_path = r"D:\DiGuo_ZDH\log"


# 创建log时取一个名字 日志可定位到哪一个模块
class Log:
    def __init__(self, name=None):
        # 文件的命名
        self.logname = os.path.join(log_path, "%s.log" % time.strftime("%Y_%m_%d"))
        self.logger = logging.getLogger(name)
        self.logger.setLevel("DEBUG")
        # 日志输出格式
        pattern = '[%(asctime)s]-[%(name)s]-[%(levelname)s]:%(message)s'
        self.formatter = logging.Formatter(pattern)

    def __console(self, level, message):
        # 创建一个FileHandler 用于写到本地
        fh = logging.FileHandler(self.logname, "a", encoding="utf-8")
        if res:
            fh_level = DoPeiZhi(t1_pth).get_strdata("log", "outlevel")
            fh.setLevel(fh_level)
        else:
            fh_level = DoPeiZhi(t2_pth).get_strdata("log", "outlevel")
            fh.setLevel(fh_level)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # 创建一个StreamHandler 用于输出到控制台
        ch = logging.StreamHandler()
        if res:
            ch_level = DoPeiZhi(t1_pth).get_strdata("log", "outlevel")
            ch.setLevel(ch_level)
        else:
            ch_level = DoPeiZhi(t2_pth).get_strdata("log", "outlevel")
            ch.setLevel(ch_level)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == "debug":
            self.logger.debug(message)
        elif level == "info":
            self.logger.info(message)
        elif level == "waring":
            self.logger.warning(message)
        elif level == "error":
            self.logger.error(message)
        else:
            self.logger.critical(message)

        # 为避免日志重复问题
        self.logger.removeHandler(fh)
        self.logger.removeHandler(ch)
        # 关闭打开的文件
        fh.close()
        ch.close()

    def debug(self, message):
        self.__console("debug", message)

    def info(self, message):
        self.__console("info", message)

    def waring(self, message):
        self.__console("waring", message)

    def error(self, message):
        self.__console("error", message)

    def critical(self, message):
        self.__console("critical", message)


if __name__ == '__main__':
    log = Log()
    log.info("这是一个严重的错误".center(20, "-"))
