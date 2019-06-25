import unittest
from selenium import webdriver
import ddt

from PO_v1.PageObjects.longin_page import LoginPage
from PO_v1.PageObjects.index_page import IndexPage
from PO_v1.TestDatas import login_datas as id
from PO_v1.TestDatas import Comm_Datas as cd

#用例三部曲：前置、步骤、断言
@ddt.ddt
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 前置 -打开网页。启动浏览器
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("{}/Index/login.html".format(cd.base_url))

    #正常用例  - 登陆+首页
    def test_login_2_success(self):
        #步骤 - 登录操作 -  登录页面
        LoginPage(self.driver).login(id.success_data["user"],id.success_data["passwd"]) #测试对象+测试数据
        #断言1. - 页面是否存在   我的账户   元素
        self.assertTrue(IndexPage(self.driver).check_nick_name_exists())
        #断言2.url是否跳转
        self.assertEqual(self.driver.current_url,id.success_data["check"])  #current_url获取当前页面的url


    #异常用例 -密码为空、用户名为空、用户名不正确、
    @ddt.data(*id.wrong_datas)  # ddt循环数据，#装饰测试方法，接收可迭代数据,
    def test_login_1_failed_by_no_passwd(self,data):
        # 步骤 - 登录操作 -  登录页面  - 密码为空  18684720553
        LoginPage(self.driver).login(data["user"], data["passwd"])
        # 断言 - 面页的提示内容为：请输入密码
        self.assertTrue(data["check"],LoginPage(self.driver).get_error_msg_from_loginFrom())

    @ddt.data(*id.fail_datas)
    def test_login_0_failed_by_fail_datas(self,data):
        # 步骤 - 登录操作 -  登录页面  - 未注册的号码  18600000000
        LoginPage(self.driver).login(data["user"], data["passwd"])
        # 断言 - 面页的提示内容为：此账号没有经过授权，请联系管理员!
        self.assertTrue(data["check"], LoginPage(self.driver).get_error_msg_from_pageCenter())


    # 异常用例 -无用户名
    # def test_login_failed_by_no_user(self):
    #     # 步骤 - 登录操作 -  登录页面  - 手机号错误  18684720553
    #     LoginPage(self.driver).login("186847205", "python")
    #     # 断言 - 面页的提示内容为：请输入密码
    #     self.assertTrue("请输入手机号", LoginPage(self.driver).get_error_msg_from_loginFrom())

    # # 异常用例 - 错误的手机号
    # def test_login_failed_by_wrong_user_formater(self):
    #     # 步骤 - 登录操作 -  登录页面  - 用户名错误  15717481995
    #     LoginPage(self.driver).login("1868472", "python")
    #         # 断言 - 面页的提示内容为：请输入密码
    #     self.assertTrue("请输入正确的手机号", LoginPage(self.driver).get_error_msg_from_loginFrom())

    @classmethod
    def tearDownClass(cls):
        #关闭浏览器，
        cls.driver.quit()  #关闭所有

    def tearDown(self):
        #刷新当前页面
        self.driver.refresh()


