import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from os.path import join, dirname
from dotenv import load_dotenv

#Loading .env file
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

# Using this to check if its the first time of the day or not
# Default initiated with True.
# instantiate a chrome options object so you can set the size and headless preference
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# download the chrome driver from https://sites.google.com/a/chromium.org/chromedriver/downloads and put it in the
# current directory
chrome_driver = os.getcwd() + "/chromedriver"
print(chrome_driver)

def keka_logout():
    browser = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
    print('Logout Process Started: ')

    browser.get("https://discidium.keka.com/#/home")
    print('Website Opened')

    time.sleep(5)

    email = browser.find_element_by_xpath('//*[@id="email"]')
    email.send_keys(EMAIL) # Enter your email here
    print('Email Entered')

    password = browser.find_element_by_xpath('//*[@id="password"]')
    password.send_keys(PASSWORD) # Enter your password here
    print('Password Entered')


    time.sleep(5)

    login_button = browser.find_element_by_xpath('//*[@id="login-container-center"]/div/div/form/div/div[4]/div/button[1]')
    login_button.click()
    print('Login Button Clicked')


    time.sleep(15)

    web_clockout_button = browser.find_element_by_xpath('//*[@id="attendance-widget"]/div/div[2]/div/div[1]/div[2]/input')
    web_clockout_button.click()
    print('WebClock Out Button Clicked')

    time.sleep(5)

    web_clockout_confirm_button = browser.find_element_by_xpath('//*[@id="attendance-widget"]/div/div[2]/div/div[1]/div[2]/div[2]/input[2]')
    web_clockout_confirm_button.click()
    print('Confirmed WebClock Out')


    time.sleep(5)

    location_request_button = browser.find_element_by_xpath('//*[@id="ng-app"]/body/div[1]/div/div/div[3]/button')
    location_request_button.click()
    print('Rejected location request')

    time.sleep(15)
    print('Successfully logged out')
    f = open("status_storage.txt", "w")
    f.write("True")
    f.close()

    time.sleep(20)
    print time.strftime("Cron Successfully ran last at: " + "%Y-%m-%d %H:%M")
    browser.quit()


keka_logout()
