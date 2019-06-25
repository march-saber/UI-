from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time

class LoginPage:
    #属性
    def __init__(self,driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver

    #登录功能
    def login(self,user,passwd):
        #等待
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.XPATH,'//input[@name="phone"]')))
        #输入用户名，输入密码，点击登录
        self.driver.find_element_by_xpath('//input[@name="phone"]').send_keys(user)
        self.driver.find_element_by_xpath('//input[@name="password"]').send_keys(passwd)
        self.driver.find_element_by_xpath('//button[@type="button"]').click()

    # //divp[@class="from-error-info"]
    # 获取表单区域的错误信息
    def get_error_msg_from_loginFrom(self):
        """
        获取的是没有输入密码和账号时的错误信息，类似提示信息
        :return: 返回错误信息文本内容
        """
        loc = (By.XPATH,'//div[@class="form-error-info"]')
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(loc))
        time.sleep(0.5)
        return self.driver.find_element(*loc).text


    #//div[@class="layui-layer-content"]
    #获取面页中间的错误信息
    def get_error_msg_from_pageCenter(self):
        """
        获取没有注册过的手机号的提示，所有类似提示弹窗
        :return:返回错误信息的文本值
        """
        loc = (By.XPATH,'//div[@class="layui-layer-content"]')
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc))
        return self.driver.find_element(*loc).text


    # def input_user(self):
    #     pass
    #
    # def input_passwd(self):
    #     pass
    #
    # def click_login_button(self):
    #     pass

