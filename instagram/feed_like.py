# -*- coding: utf-8 -*-
"""

Created on Tue Aug  7 16:17:31 2018

@author: YOONHOI

인스타그램 피드 좋아요
"""

ID = input('전화번호, 사용자 이름 또는 이메일 : ')
PW = input('비밀번호 : ')
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


#피드 좋아요 
for i in range(1,number+1):
    path = '//*[@id="react-root"]/section/main/section/div/div[1]/div/article['+str(i)+']/div[2]/section[1]/span[1]/button'
    heart = driver.find_element_by_xpath(path)
    heart.click()
    time.sleep(10)
