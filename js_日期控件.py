from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
# 1.允许你编辑，直接输入日期。--就直接输入

#执行js
js_pha = 'var a = document.getElementById("train_date");' \
         'a.readOnly = false;' \
         'a.value = "2019-07-01";'  #js语句，查找修改元素，var a = ...  ,car表示定义一个

driver.execute_script(js_pha)

# send_keys去输入内容，提交的时候还，面页提示我内容为空？
# 这就要dom对象去设置他的value值。。--就是
