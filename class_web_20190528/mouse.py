from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
#先找到设置
ele = driver.find_element_by_xpath("//div[@id='u1']//a[@name='tj_settingicon']")
# #1、实例化
# ac = ActionChains(driver)
#
# #2、鼠标操作
# ac.move_to_element(ele) #悬浮
# ac.click()  #点击
#
# # 3、执行动作
# ac.perform()

#上述操作可优化：链式操作，因为返回的是.self（他本身）
ActionChains(driver).move_to_element(ele).click(ele).perform()

#选择下拉列表当中的值
# //a[text()="高级搜索"]
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//a[text()="高级搜索"]'))) #等待元素可见
driver.find_element_by_xpath('//a[text()="高级搜索"]').click()  #点击操作


#select类来处理select/option元素
#可以通过value，index，text三种方式选择option对于的值

# 1、找到select元素对象，实例化Select类
WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//select[@name="ft"]')))
s = Select(driver.find_element_by_xpath('//select[@name="ft"]'))

#2、选择下拉列表的值
#2.1 value属性值
time.sleep(3)
s.select_by_value("ppt")

time.sleep(3)
s.select_by_index(3)  #下标从0开始

time.sleep(3)
s.select_by_visible_text("所有格式")


#iframe 和alert弹出框  -driver.switch_to.frame()/alert-Alert类
#鼠标操作 -ActionChains 类
#下拉列表  -Select 类