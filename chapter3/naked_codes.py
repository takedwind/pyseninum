from selenium import webdriver
from time import sleep

# 启动浏览器
driver = webdriver.Chrome('../drivers/chrome_driver.exe')

# 打开目标网站
driver.get('http://127.0.0.1/zentao/user-login.html')

# 登录
driver.find_element_by_id('account').send_keys('admin')
driver.find_element_by_name('password').send_keys('admin123456')
driver.find_element_by_id('submit').click()

# 登录断言
sleep(1)
if driver.find_element_by_xpath('//span[@class="user-name"]').text == 'admin':
    print('pass')
else:
    print('fail')

# 检索bug
driver.find_element_by_id('searchInput').send_keys('1')
driver.find_element_by_id('searchGo').click()

# 检索结果断言
if driver.find_element_by_xpath('//span[@class="label label-id"]').text == '1':
    print('pass')
else:
    print('fail')

# 关闭浏览器
driver.quit()
