import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

pwd = os.getcwd()
browser = webdriver.Chrome(pwd + 'chromedriver')

def keka_logout():
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

    web_clockout_button = browser.find_element_by_xpath('//*[@id="attendance-widget"]/div/div[2]/div/div[1]/div[2]/input')
    web_clockout_button.click()

    time.sleep(5)

    web_clockout_confirm_button = browser.find_element_by_xpath('//*[@id="attendance-widget"]/div/div[2]/div/div[1]/div[2]/div[2]/input[2]')
    web_clockout_confirm_button.click()

    time.sleep(20)

    browser.quit()


keka_logout()
