import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

pwd = os.getcwd()

browser = webdriver.Chrome(pwd + '/chromedriver')

def keka_login():
    browser.get("https://discidium.keka.com/#/home")

    time.sleep(5)

    email = browser.find_element_by_xpath('//*[@id="email"]')
    email.send_keys("") # Enter your email here

    password = browser.find_element_by_xpath('//*[@id="password"]')
    password.send_keys("") # Enter your password here

    time.sleep(5)

    login_button = browser.find_element_by_xpath('//*[@id="login-container-center"]/div/div/form/div/div[4]/div/button[1]')
    login_button.click()

    time.sleep(15)

    web_clockin_button = browser.find_element_by_xpath('//*[@id="attendance-widget"]/div/div[2]/div/div[1]/div[2]/input[1]')
    web_clockin_button.click()

    time.sleep(5)

    note_text_area = browser.find_element_by_xpath('//*[@id="ng-app"]/body/div[1]/div/div/div[2]/form/div[1]/div/textarea')
    note_text_area.send_keys("Starting now")

    time.sleep(5)

    request_button = browser.find_element_by_xpath('//*[@id="ng-app"]/body/div[1]/div/div/div[2]/form/div[2]/div/div/input[1]')
    request_button.click()

    time.sleep(15)

    browser.quit()

keka_login()
