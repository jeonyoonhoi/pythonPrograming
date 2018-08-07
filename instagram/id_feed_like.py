# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 16:32:18 2018

@author: YOONHOI

인스타그램 특정 타임라인 좋아요

"""


ID = input('전화번호, 사용자 이름 또는 이메일 : ')
PW = input('비밀번호 : ')
goID = input("누구의 타임라인을 방문하시겠습니까?")
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

instagramURL = 'https://www.instagram.com/'
timelineURL = instagramURL+goID+'/'
driver.get(timelineURL)
#여기까지하면 그 사람의 타임라인을 방문한 상태

#행 1,2,3,4
for i in range(1,number+1):
    #열 1,2,3
    for j in range(1,4):
        #사진의 xpath로 접근
        photo_xpath='//*[@id="react-root"]/section/main/div/div[2]/article/div[1]/div/div['+str(i)+']/div['+str(j)+']/a'
        #사진 클릭
        temp = driver.find_element_by_xpath(photo_xpath)
        temp.click()
        time.sleep(2)
        
        #좋아요가 눌려있는지확인
        #이미눌렀으면 스킵
        
        #좋아요 누르기
        driver.find_element_by_xpath('//span[@aria-label="좋아요"]').click()
        
        #창 닫기   /html/body/div[3]/div/button
        driver.find_element_by_xpath('/html/body/div[3]/div/button').click()
        time.sleep(2)
        
#이미 좋아요가 눌러져 있을 ㄸㅐ 오류가 남

