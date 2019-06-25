from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time

class IndexPage:

    def __init__(self,driver):
        self.driver = driver

    def check_nick_name_exists(self):
        """
        检查附近元素是否存在
        :return:存在返回True,不存在返回False
        """
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.XPATH,"//a[text()='关于我们']")))
        time.sleep(0.5)
        try:
            self.driver.find_element_by_xpath('//a[@href="/Member/index.html"]')
            return True
        except:
            return False

    #//divp[@class="from-error-info"]
    #获取表单区域的错误信息

    # def check_passwd_exists(self):
    #     """
    #     检查，密码是否输入
    #     :return: 输入返回True，没有输入返回False
    #     """
    #     WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.XPATH,'//div[text()="请输入密码"]')))
    #     try:
    #         self.driver.find_element_by_xpath('//div[text()="请输入密码"]')
    #         return True
    #     except:
    #         return False