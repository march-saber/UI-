from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')

#1、通过元素ID属性找到元素
# ele = driver.find_element_by_id('kw')  #返回的WebElement对象，封装了元素
# print(ele.tag_name)  #找到元素获取标签名
# print(ele.get_attribute('class'))  #获取class属性值

#2、name属性
# driver.find_element_by_name('wd')  #找一个单一的元素,从上往下，符合条件的第一个元素
# ele_list = driver.find_elements_by_name("wd")  #找到所有匹配的元素，，返回的是列表，每一个都是WEblement对象
# print(ele_list[0].tag_name)

#3、class属性  只能选择一个class值
# driver.find_element_by_class_name('')
# driver.find_elements_by_class_name('')

# 4、标签名 tag_name
# driver.find_element_by_tag_name('')
# driver.find_elements_by_tag_name('')

#5，6  链接元素  link   text   #完全匹配  #模糊匹配
# driver.find_element_by_link_text("更多产品")  #完全匹配
# driver.find_element_by_partial_link_text('更多')  #模糊匹配

#7，8、 xpath  css 两种方法
#xpath定位：
#绝对（路径）定位，严格按照路径和位置来定位元素，以/开头， 父/子关系
#相对路径，参照物：整个HTML ，只要能够在这个面页当中，找到符合属性的元素，以//开头
# //*[@id='kw']
# /html/body/div[2]/div/from/div[1]/input
# //input[@name="phone"]
# //input[@name="phone" and @datatype="m11"]  #同时满足两个条件
# //input[@name="phone" or @datatype="m11"]   #满足其中一个

#1、//标签名[@属性名称=属性值]
#2、逻辑运算符：and  or  //标签名[@属性名称=属性值 and @属性名称=属性值]
# driver.find_element_by_xpath('//input[@name="phone"]')
# driver.find_elements_by_xpath('')

#3、元素的文本内容：  //标签名[text()="元素的文本内容"]    #文本内容完全匹配

#4、文本内容：文本内容/属性值   contains(text()/@属性，部分值)
    # //标签名[contains(text()="元素的文本内容")]  #太长了的话用这两种
    # //标签名[contains(@属性，"部分属性值"]    #太长了的话用这两种   ——>//input[contains(@value,"百度")]

# 5、当你不能通过自己的属性唯一找到的时候，就要利用层级关系
#5.1、层级定位  第一种方式  ：  //div[@id='ul']//a[@name='ti_login']
       # 后一条件，是在前一个得到的结果之内去搜索

#5.2、层级定位 -- 轴定位   #表达式： /轴定位名称::标签名[属性表达]
     #兄弟姐妹 --直系的    有比你大的，有比你小的
     #preceding-sibing : 哥哥姐姐
     #following-sibing : 弟弟妹妹
     #//a[@name='tj_trxueshu']/following-sibling::a[@name='tj_login']
     #//a[@name='tj_settingicon']/preceding-sibling::a[@name='tj_login']

     #  爸爸：parent   祖先：ancestor
     #//     /parent::div//a[@name='ti_login']   -->//a[@name='tj_trtieba']/parent::div//a[@name='tj_login']
            # /parent表示同一个爸爸
     #//a[text()='百度首页']/parent::div/following-sibling::div//a[@name='tj_login']   表兄妹做法

