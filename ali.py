from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
with open('../workday.txt', 'r') as r:
    username, password = r.readline().split(',')

chrome = webdriver.Chrome()
chrome.get('https://free.aliyun.com/ntms/free/experience/getTrial.html')
chrome.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[3]/a[1]').click()
"""time.sleep(1)
chrome.switch_to.frame(chrome.find_element_by_id('alibaba-login-box'))
user = chrome.find_element_by_xpath('//*[@id="fm-login-id"]')
action = ActionChains(chrome).key_down(Keys.TAB).key_up(Keys.TAB).key_down(Keys.TAB).key_up(Keys.TAB).send_keys(password).perform()
chrome.get(r'https://passport.alibaba.com/mini_login.htm?lang=zh_CN&appName=aliyun&appEntrance=aliyun&styleType=vertical&bizParams=&notLoadSsoView=&notKeepLogin=true&isMobile=false&regUrl=https%3A%2F%2Faccount.aliyun.com%2Fregister%2Fregister.htm&returnUrl=https%3A%2F%2Faccount.aliyun.com%3A443%2Flogin%2Flogin_aliyun.htm&rnd=0.5954296379346966')
chrome.find_element_by_xpath('//*[@id="fm-login-id"]').send_keys(username)
chrome.find_element_by_xpath('//*[@id="fm-login-password"]').send_keys(password)
chrome.find_element_by_xpath('//*[@id="fm-login-submit"]').click()
time.sleep(3)
chrome.switch_to.default_content()"""
input('Input anything to start:')
while True:
    chrome.find_element_by_xpath('//*[@id="guid-723146"]/div/div[2]/div[2]/div/div[1]/div[3]/div[2]/a').click()
    time.sleep(0.5)
    chrome.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[3]/a').click()
    time.sleep(0.5)

#sreach_window=chrome.current_window_handle
#chrome = chrome.switch_to_window(sreach_window)