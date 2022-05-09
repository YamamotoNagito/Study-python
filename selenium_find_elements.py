from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()

# idを指定する
driver.find_element_by_id('id')

# name属性を指定
driver.find_element_by_name('name')

# xpathを指定
driver.find_element_by_xpath('xpath')

driver.find_element_by_link_text('link_text')

driver.find_element_by_partial_link_text('partial_link_text')

# tagの名前を指定 h1,pタグetc
driver.find_element_by_tag_name('tag_name')

driver.find_element_by_css_selector('css_selector')

# class_nameを指定
driver.find_element_by_class_name('class_name')

# 要素を指定
driver.get_attribute('value')

# classが複数ある場合については配列の何番目にあるのかを指定すること
driver.find_elements_by_class_name('class_name')[0] #elements : 複数の要素がある場合に用いる