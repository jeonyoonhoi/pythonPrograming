# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 17:49:26 2018

@author: YOONHOI

원하는 지역 좋아요 
"""



ID = input('전화번호, 사용자 이름 또는 이메일 : ')
PW = input('비밀번호 : ')
location = input('원하는 지역명 입력 : ')
number = 10

from selenium import webdriver
import time

#로그인 페이지 접속
driver = webdriver.Chrome('C:/Users/YOONHOI/Desktop/chromedriver')
driver.get('https://www.instagram.com/accounts/login/')
#driver.find_element_by_xpath(""" //div*[@aria-label='Any Time'] """).click()

#로그인 과정
spaceID = driver.find_element_by_xpath(" //input[@aria-label='전화번호, 사용자 이름 또는 이메일']")
spaceID.send_keys(ID)

spacePW = driver.find_element_by_xpath(" //input[@aria-label='비밀번호']")
spacePW.send_keys(PW)

driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/span/button').click()
time.sleep(10)

#검색 element에 키워드 넘긴다. //*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input

element_explore = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
element_explore.send_keys(location)
time.sleep(10)

#space_icon = driver.find_element_by_xpath('//div[@class="nebtz coreSpriteLocation"]')

#장소 아이콘 으로 찾고 싶은데 왜 안될까 
driver.find_element_by_class_name('nebtz coreSpriteLocation').click()

