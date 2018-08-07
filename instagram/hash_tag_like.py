# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 17:44:36 2018

@author: YOONHOI

인스타그램 특정 해시태그 좋아요
"""



ID = input('전화번호, 사용자 이름 또는 이메일 : ')
PW = input('비밀번호 : ')
hash_tag = input('원하는 해시태그 입력 : ')
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


#해시태그
explore_tags_URL = 'https://www.instagram.com/explore/tags/'+ hash_tag +'/'
driver.get(explore_tags_URL)

#인기게시글(상단 9개)
for i in range(1,4):
    #열 1,2,3
    for j in range(1,4):
        #사진의 xpath로 접근
        photo_xpath='//*[@id="react-root"]/section/main/article/div[1]/div/div/div['+str(i)+']/div['+str(j)+']/a'
        #사진 클릭
        driver.find_element_by_xpath(photo_xpath).click()
        time.sleep(2)
        
        #좋아요가 눌려있는지확인
        #이미눌렀으면 스킵
        
        #좋아요 누르기
        driver.find_element_by_xpath('//span[@aria-label="좋아요"]').click()
        time.sleep(2)
        
        #창 닫기
        driver.find_element_by_xpath('/html/body/div[3]/div/button').click()
        time.sleep(2)
 


#최근게시글
for i in range(1,number+1):
    #열 1,2,3
    for j in range(1,4):
        #사진의 xpath로 접근
        photo_xpath='//*[@id="react-root"]/section/main/article/div[2]/div/div['+str(i)+']/div['+str(j)+']/a'
        #사진 클릭
        driver.find_element_by_xpath(photo_xpath).click()
        time.sleep(2)
        
        #좋아요가 눌려있는지확인
        #이미눌렀으면 스킵
        
        #좋아요 누르기
        driver.find_element_by_xpath('//span[@aria-label="좋아요"]').click()
        time.sleep(2)
        
        #창 닫기
        driver.find_element_by_xpath('/html/body/div[3]/div/button').click()
        time.sleep(2)
               