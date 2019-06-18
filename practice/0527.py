from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")  #get等待静态界面加载完成

#当操作带来面页的变化时，请一定要等待
driver.find_elements_by_xpath("//div[@id='u1']//a[@name='tj_login']").click()

#1.傻等
# time.sleep(3) #傻等3?秒

#2.智能等待2.智能等待，设置等待上限，超过就提示超时TimeoutExcept：
#设置全局等待时间：
#driver.implicitly_wait(30)  #全局等待，每个find_element查找元素的时候，如果该元素没有出现，就等待30秒，单位秒

#3.智能等待：如果十秒内出现了，我就开始下一步操作。设置一个上线
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#元素存在：（HTML里面存在，能找到）
#元素可见（存在并且可见-看得见大小-可见才可操作）
#元素可用（可见之后，才有可用的可能性。只读/不可点击-不可用）

#等待条件表达
#locator = （定位类型，定位表达式）
locator = (By.ID,"'TANGRAM__PSP_10__footerQrcodeBtn'")
# EC.visibility_of_element_located(locator=locator)    #元素可见,条件
#等待元素可见
WebDriverWait(driver,30).until(EC.visibility_of_element_located(locator=locator))
#辅助 -0.5秒
time.sleep(0.5)
#点击元素
driver.find_element_by_id('TANGRAM__PSP_10__footerQrcodeBtn').click()

#智能等待：如果十秒内出现了，我就开始下一步操作。设置一个上线


