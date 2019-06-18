from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(30)  #设置全局等待时间
driver.get("http://www.baidu.com")

#输入柠檬班
# driver.find_element_by_id("kw").clear()  #清除输入框里的内容，清除文本
driver.find_element_by_id("kw").send_keys("柠檬班")   #输入操作
driver.find_element_by_id("su").click()  #点击百度一下

#等待

locator = (By.XPATH,'//a[text()="_腾讯课堂"]')
WebDriverWait(driver,30).until(EC.visibility_of_element_located(locator))  #确保元素可见

#点击柠檬班-腾迅课堂
# driver.find_element_by_xpath('//a[text="_腾讯课堂"]').click()

#方式一：
driver.find_element(*locator).click()  #等同上面的操作，解包

# #打开新窗口
# #1、获取所有的窗口
# handles = driver.window_handles
# print(handles)
# #当前窗口的handle
# print(driver.current_window_handle)
# #切换窗口
# driver.switch_to.window(handles[-1])
# print("切换之后的窗口为：",driver.switch_to.window(handles[-1]))


#方式二
#step1:获取窗口数
handles = driver.window_handles  #查询窗口总数，此时只有1个窗口
#step2:执行打开新窗口的操作
driver.find_element(*locator).click()  #等同上面的操作，解包

#step3:确认新的窗口出现了，再去操作它，等待新的窗口出现
#EC.new_window_is_opened   #比窗口总数大小，传一个窗口总数
WebDriverWait(driver,10).until(EC.new_window_is_opened(handles))  #2>1
#step4:再次获取窗口的handles
handles = driver.window_handles
#step5：切换到新窗口
driver.switch_to.window(handles[-1])

#新的窗口当中，点击课程
#等待
locator = (By.XPATH,"//section[@class='section-main']//h2[contains(text(),'课程')]")
WebDriverWait(driver,20).until(EC.visibility_of_element_located(locator))
driver.find_element(*locator).click()

#iframe里的HTML切换：
#方式一：
# #先等待iframe可用
# driver.switch_to.frame(4)
# driver.switch_to.frame("login_frame_qq")
# driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@name="login_frame_qq"]'))
#
# #方式二：
# # EC.frame_to_be_available_and_switch_to_it("login_frame_qq")#确认iframe可用并切进，可以传入的下标、name属性、对象
# WebDriverWait(driver,20).until(EC.frame_to_be_available_and_switch_to_it("login_frame_qq"))

# 我要从iframe里面切到默认的HTML当中
driver.switch_to.default_content()
#切换到上一个父iframe
driver.switch_to.parent_frame()




#alert弹窗：
#2.等待alert弹窗出现
WebDriverWait(driver,20).until(EC.alert_is_present())
#3.切换
alert = driver.switch_to.alert
#4、使弹窗消失
print(alert.text)  #获取alert弹窗里面的内容
alert.accept()  #确认
alert.dismiss()  #取消按钮
alert.send_keys()  #输入内容

#进行后续其他元素操作