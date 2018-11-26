from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException
import time
import pymysql

conn = pymysql.connect(host='host_name', user='user_name', password='password', db='db_name', charset='utf8')

curs = conn.cursor()

photo = []
name = []
birth = []
hometown = []
party = []

def politicians(i, j):
    driver = webdriver.Chrome('/chromedriver')
    driver.set_window_size(1440,1080)
    driver.implicitly_wait(3)
    driver.get('http://www.rokps.or.kr/profile/profile_number.asp')
    driver.find_element_by_xpath(
    '//*[@id="content_box"]/div/div[1]/div/form/div/select/option['+(want to know election+1)+']'
    ).click()
    driver.find_element_by_xpath(
    '//*[@id="content_box"]/div/div[1]/div/form/div/span[2]/input'
    ).click()
    driver.implicitly_wait(3)
    try: 
        driver.find_element_by_xpath(
        '//*[@id="content_box"]/div/table/tbody/tr['+str(i+1)+']/td['+str(j+1)+']/a'
        ).click()
        driver.implicitly_wait(3)
        
        photo_in = driver.find_element_by_css_selector('#printArea > div.view_con01_box > div > img')
        photo_url = photo_in.get_attribute('src')
        photo.append(photo_url)
        driver.implicitly_wait(3)
        
        name_in = driver.find_element_by_css_selector('#printArea > div.view_con01_box > dl > dt')
        name_text = name_in.text
        name.append(name_text)
        print('---'+name_text+'--- 정보 처리')
        driver.implicitly_wait(3)
        
        party_in = driver.find_element_by_css_selector('#printArea > div:nth-child(3) > p')
        party_text = party_in.text
        party_l=party_text.split('\n')
        for i in range(len(party_l)):
            if party_l[i].find('18') != -1:
                in_party = party_l[i]
        party_no = in_party[16:]
        if 'party_name1' in party_no:
            party_num = 0
        elif 'party_name2' in party_no:
            party_num = 1
        elif 'party_name3' in party_no:
            party_num = 2
        else:
            party_num = 4
        party.append(party_num)
        driver.close()
    except NoSuchElementException:
        pass
    
for i in range(0, x): #x = count-1 of photo rows in page
    for j in range(0, 10):
        politicians(i, j)
        time.sleep(1)
print("---정보 처리 끝---")
