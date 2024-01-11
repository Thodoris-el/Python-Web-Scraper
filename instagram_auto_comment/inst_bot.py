
import requests
from bs4 import BeautifulSoup
import csv
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
from selenium.webdriver.common.keys import Keys
import random


def send_keys_custom(controller, keys, min_delay=0.1, max_delay = 0.5):
    for key in keys:
        controller.send_keys(key)
        time.sleep(random.uniform(min_delay, max_delay))

options = Options()
#proxy = "34.162.156.215:8585"
#options.add_argument('--proxy-server=%s' % proxy)
#options.add_argument("ignore-certificate-errors")
options.headless = True

msg = ['msg1', 'msg2', 'msg3', 'msg4', 'msg5', 'msg6', 'msg7', 'msg8', 'msg9', 'msg10', 'msg11', 'msg12']
acc = ['@account1', '@account2', '@account3']
login_url = "https://www.instagram.com"

driver = webdriver.Chrome(executable_path=r'C:\Users\dionn\Thodoris\Go_Project\Python web scraping\chromedriver.exe', options=options)
driver.implicitly_wait(10)
driver.get(login_url)
time.sleep(5)

button = driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]")

driver.execute_script("arguments[0].click();",button)
time.sleep(5)


username = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
username.send_keys("user_email")

password = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
password.send_keys("password")

sign_in = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
driver.execute_script("arguments[0].click();", sign_in)
time.sleep(10)

#pic url
pic_url = "https://www.instagram.com/reel/C1ueFdBx452/"
driver.get(pic_url)
time.sleep(10)
print("Start Commenting---")
count = 0
while count < 5:
    comment = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[4]/section/div/form/div/textarea')
    comment.click()
    time.sleep(2)
    comment = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[4]/section/div/form/div/textarea')
    acc1 = random.choice(acc)
    acc2 = random.choice(acc)
    while ( acc1 == acc2):
        acc2 = random.choice(acc)
    text = acc1 + " " + acc2 + " " + random.choice(msg)
    send_keys_custom(controller=comment, keys=text)
    print(text)

    button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[4]/section/div/form/div/div[2]/div')
    driver.execute_script("arguments[0].click()", button)

    time.sleep(random.uniform(150, 250))
    count += 1
    print("Comment " + str(count) + "done-----------------")

