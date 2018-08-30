import time
import random
from selenium import webdriver
from urllib.parse import quote


id = 'id'
password = 'password'

timeline_like_count = 120
hash_tags = ['코딩', '빅데이터','보아즈']
hash_tags_count = 60

browser = webdriver.Chrome('chromedriver')
browser.get('https://instagram.com/')

def login(_id, _password):
    
    #인스타그램 로그인 구현 
    spaceID = driver.find_element_by_xpath(" //input[@aria-label='전화번호, 사용자 이름 또는 이메일']")
    spaceID.send_keys(_id)

    spacePW = driver.find_element_by_xpath(" //input[@aria-label='비밀번호']")
    spacePW.send_keys(_password)

    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/span/button').click()
    
    pass

def timeline_like(timeline_like_count):
    
    #타임라인 좋아요 구현
    for i in range(1,timeline_like_count+1):
        path = '//*[@id="react-root"]/section/main/section/div/div[1]/div/article['+str(i)+']/div[2]/section[1]/span[1]/button'

        heart = driver.find_element_by_xpath(path)
        heart.click()
        time.sleep(1)
    
    pass

def hash_tags_like(hash_tags, hash_tags_count):
    #해시태그 좋아요 구현
    
    explore_tags_URL = 'https://www.instagram.com/explore/tags/'+ hash_tags +'/'
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
    for i in range(1,hash_tags_count+1):
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

    
    pass

login(id, password)
timeline_like(timelinke_like_count)
hash_tags_like(hash_tags, hash_tags_count)

browser.quit()
