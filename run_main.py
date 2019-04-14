#- *- coding:utf-8 -*-

import unittest
import time
import HTMLTestRunner
import os
from testcase.testadd import TestAdd  #加载测试用例
from testcase.duexcel import DoExcel   #加载读取文件的类


def add_case(case_path,rule):  #case_path,rule  有discover 时 需要入参
    """加载所有的测试用例"""
    suite=unittest.TestSuite()
    # cases=DoExcel("./testcase/case_data.xlsx").get_sheet("add")
    #print(cases)
    # test_data=[
    #     [0,0,0],
    #     [1,1,2],
    #     [-1,1,0]
    # ]
    # for item in test_data:
    #     suite.addTest(TestAdd(item[0], item[1], item[2], "test_add"))


    #  使用超继承的方法
    # for case in cases:
    #     suite.addTest(TestAdd(case.case_id,case.a,case.b,case.excepted,"test_add"))

    #定义discover 方法参数
    discover=unittest.defaultTestLoader.discover(case_path,
                                                 pattern=rule,
                                                 top_level_dir=None)
    suite.addTests(discover)
    return suite

def run_case(all_case,report_path):
    """执行所有的用例，并把结果写入测试报告"""
    now=time.strftime("%Y_%m_%d_%H_%M_%S")
    report_path=os.path.join(report_path,now+"result.html")
    fp=open(report_path,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,
                                         title="自动化测试报告",
                                         description="用例执行情况")
    #调用add_case函数的返回值
    runner.run(all_case)
    fp.close()

def get_report_file(report_path):
    """获取报告发送邮件时需要用到"""
    pass

if __name__ == '__main__':
    # 测试用例的路径
    case_path=r"D:\DiGuo_ZDH\testcase"
    rule="test*.py"
    all_case=add_case(case_path,rule)
    # 生成报告的路径
    report_path=r"D:\DiGuo_ZDH\report"
    run_case(all_case,report_path)

