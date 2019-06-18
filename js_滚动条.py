from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#可见/视区域   -要滚动到可见区域，进行操作


#大部分系统在元素操作时，如果元素不在可见区域，随着操作会自动到可见区域


driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
#组合键的输入，Keys类
driver.find_element_by_id("kw").send_keys("柠檬班",Keys.ENTER)

locator = (By.XPATH,"//a[contains(text(),'全部课程_在线 培训 视频 教程_腾讯课堂')]")
WebDriverWait(driver,20).until(EC.visibility_of_element_located(locator))

#要滚动的元素
ele = driver.find_element_by_xpath("//a[contains(text(),'全部课程_在线 培训 视频 教程_腾讯课堂')]")

#执行js语句
# arguments[0].scrollIntoView()   -面页顶端
driver.execute_script("arguments[0].scrollIntoView();",ele)

#页面低端
# arguments[0].scrollIntoView(false)   -页面底端
# driver.execute_script("arguments[0].scrollIntoView(false);",ele)

# scrollIntoViewIfNeeded   自动滚动，可网上自己去了解

# 移动到面页底部
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

#移动到面页顶部：
driver.execute_script("window.scrollTo(document.body.scrollHeight)")