#- *- coding:utf-8 -*-

import unittest
from common.deebug import add
from fools.log_pz import Log
from common.path_file import FilePath
from testcase.duexcel import DoExcel
# from ddt import ddt,data,unpack,file_data  #  ddt实现
from common.re_test import new_replace
from common.ddt import ddt,data,unpack,file_data  #  修改ddt源码 测试方法上加上title
from common.model_lineno import get_cur_info


@ddt
class TestAdd(unittest.TestCase):
    """测试加法"""
    log=Log("case")
    #获取文件路径
    pth = FilePath("testcase", "case_data.xlsx").filepath()
    t = DoExcel(pth)
    cases=t.get_sheet("add")

    # 使用 超继承的方法
    # def __init__(self,case_id,a,b,excepted,methodName): #重写
    #     super(TestAdd, self).__init__(methodName)
    #     self.case_id=case_id
    #     self.a=a
    #     self.b=b
    #     self.excepted=excepted

    def setUp(self):

        # print("测试要开始了")
        pass

    @data(*cases)
    def test_add(self,case):
        try:
            # case.a  与case.b 的值需要替换成replace的值
            a1=new_replace(str(case.a))
            b1=new_replace(str(case.b))
            test_result=add(int(a1),int(b1))
            self.assertEqual(case.excepted,test_result,"定义的测试信息")
            Testresult="Pass"
            s = get_cur_info()
            self.log.info("执行第{0}条：{1}用例，结果{2}-{3}"
                          .format(case.case_id,case.title,Testresult,str(s)))
        except Exception as e:
            Testresult = "Fail"
            s=get_cur_info()
            self.log.error("执行第{0}条：{1}用例，结果{2}-{3}"
                           .format(case.case_id, case.title, Testresult,str(s)))
            raise e
        finally:
            self.t.set_sheet(case.case_id+1,6,test_result,"add")
            self.t.set_sheet(case.case_id+1,7,Testresult,"add")

    def tearDown(self):
        # print("测试结束了")
        pass

if __name__ == '__main__':
    unittest.main()