from selenium import webdriver
import time
with open('../password.txt', 'r') as r:
    username, password = r.readline().split(',')

chrome = webdriver.Chrome()
chrome.get('https://www.itjuzi.com/user/login')
time.sleep(2)
chrome.find_element_by_xpath('//*[@id="create_account_email"]').send_keys(username)
chrome.find_element_by_xpath('//*[@id="create_account_password"]').send_keys(password)
chrome.find_element_by_xpath('//*[@id="login_btn"]').click()