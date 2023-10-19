# -*- coding=utf-8 -*-
from __future__ import print_function
def progress(percent,width=50):
	'''進度列印功能
	   每次的輸入是已經完成總任務的百分之多少

	'''
	if percent >= 100:
		percent=100
  
	show_str=('[%%-%ds]' %width) %(int(width * percent/100)*"#") #字串拼接的巢狀使用
	print('\r%s %d%%' %(show_str,percent),end='')


import winsound
from selenium import webdriver
from selenium.webdriver import ActionChains 
import urllib.request
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from urllib3.exceptions import ReadTimeoutError
import os
import sys

import socket
# 設置超時(60)s
socket.setdefaulttimeout(30)

if len(sys.argv) == 4:
    page_jump_num  = int(sys.argv[1])
    page_input_num = int(sys.argv[2])
    resume_index   = int(sys.argv[3])
else:
    page_jump_num  = 0
    page_input_num = 1
    resume_index   = 0
    '''
    winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
    #print("等待輸入上次載到的進度,(初始 = 010)", page_jump_num, page_input_num, start)
    print("等待輸入上次載到的進度,(初始 = 010)")
    print('page_jump_num = ')
    page_jump_num = int(input())
    print('page_input_num = ')
    page_input_num = int(input())
    print('page index = ')
    resume_index = int(input())
    '''

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.headless = True
driver = webdriver.Chrome(options=options)   # 注意，這裡如果找不到，請寫你的驅動路徑在參數裡
#driver = webdriver.Chrome()
#driver.get('http://img.chinamaxx.net/n/abroad/hwbook/chinamaxx/10778600/d3af0955b99943939ac07663711f25f3/278fae0777abcef6341cd41863258cd8.shtml?tp=jpabroad&fenlei=&t=1&username=twqhdx')

def restart():
    print('restart!')
    '''
    winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
    for j in range(3,-1,-1):
        freq = 850*((1.06)**j)
        winsound.Beep(int(freq), 500)
    '''
    driver.quit()
    os.system(
        'python auto_download_book5.py ' + 
        str(page_jump_num) + ' ' +
        str(page_input_num) + ' ' +
        str(resume_index)
    )
    os.system("powershell Stop-Process -name python")
    sys.exit()


def start():
    driver.get('http://www.chinamaxx.net/SearchBooks.action') #首頁搜尋
    search = driver.find_element_by_css_selector('input#sw') #send_keys：關鍵字
    search.send_keys('中国禅宗与诗歌') # send_keys：關鍵字
    search.submit()
    sleep(5)
    driver.find_element_by_xpath(                                                                                                      #this index                    
        '/html/body/table[2]/tbody/tr/td[1]/table[2]/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td[3]/a/span/font'
        ).click() # 書名連結右鍵檢查→藍底標記之程式碼右鍵→選擇「Copy」→選擇「Copy full Xpath」→貼在上方橘色字頭尾之''內
    sleep(2)
    # 新視窗
    window_after = driver.window_handles[1]
    driver.close()
    driver.switch_to.window(window_after)
    sleep(5)
def key_in(input_format, value):
    input_format.clear()
    input_format.send_keys(value)
    input_format.submit()



try:
    start()
    page_down_botton = driver.find_element_by_link_text('Page Down')
    page_jump = driver.find_element_by_css_selector(
                'select#pagejump'
                )
    page_input = driver.find_element_by_css_selector(
                'input#pageInput'
                )
except:
    print("start fail !")
    restart()


#page_jump_num = 0
#page_input_num = 1

# get the image source
img = driver.find_elements_by_class_name(
    'readerImg'
    )



Select(page_jump).select_by_value(str(page_jump_num))
key_in(page_input,str(page_input_num))

print("continue")
sleep(10)
img = driver.find_elements_by_class_name(
    'readerImg'
    )
warrning_msg = " url is dot!"
sleep(10)
total = len(img)
print("total pages = " + str(total))
if total == 0:
    restart()
for i in range(resume_index,total):
    try:
        dot_time = 0
        url = img[i].get_attribute("src")
        '''
        url = driver.find_elements_by_xpath(
            '/html/body/div[3]/div[2]/div/div['+ str(i+1) + ']/input'
        ).get_attribute("src")
        '''
        sleep(0.5)
        while url == 'http://img.chinamaxx.net/images/dot.gif':
            sleep(0.5)
            url = img[i].get_attribute("src")
            print(warrning_msg, end = "", flush=True)
            sleep(0.5)
            print(len(warrning_msg)*"\b"+len(warrning_msg)*" "+len(warrning_msg)*"\b", end ='', flush = True)
            dot_time = dot_time + 1
            if dot_time > 60:
                print('\nNetwork conditions is not good. Re-download....')
                page_jump_num = page_jump.get_attribute("value")
                print('page_jump_num = ' + page_jump_num)
                page_input_num = page_input.get_attribute("value")
                print('page_input_num = ' + page_input_num)
                print('page_index = ' + str(i))
                # Play Windows exit sound.
                '''
                winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
                for j in range(6,-1,-1):
                    freq = 500*((1.03)**j)
                    winsound.Beep(int(freq), 500)
                '''
                exit()
        urllib.request.urlretrieve(url, "./book_test/" + str(i).zfill(3) + ".jpg")
        sleep(0.5)
        page_down_botton.click()
    except :
        print('\nNetwork conditions is not good. Re-download....')
        page_jump_num = page_jump.get_attribute("value")
        print('page_jump_num = ' + page_jump_num)
        page_input_num = page_input.get_attribute("value")
        print('page_input_num = ' + page_input_num)
        print('page_index = ' + str(i))
        resume_index = i
        # Play Windows exit sound.
        '''
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
        for j in range(6,-1,-1):
            freq = 500*((1.03)**j)
            winsound.Beep(int(freq), 500)
        #os.system('python auto_download_book5.py', page_jump_num, page_input_num, i)
        driver.quit()
        os.system('python auto_download_book5.py')
        '''
        restart()
    progress(100*(i+1)/(total))
    print(", " + str(i+1) + "/" + str(total) + " ", end = "") 
    

print ('\nfinished!')
for i in range(0,8):
    freq = 500*((1.122)**i)
    winsound.Beep(int(freq), 500)
os.system("powershell Stop-Process -name python")

#driver.quit()

#/html/body/div[3]/div[2]/div/div[230]/input
# 