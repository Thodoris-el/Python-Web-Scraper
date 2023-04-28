import requests
from bs4 import BeautifulSoup
import csv
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from webScraper import *
from selenium.webdriver.chrome.options import Options
import pandas as pd

#Url of eshop
url = 'https://www.ab.gr/eshop?amc_cid=ppc_google-search_abeshop_NA_allusers_textad_searcheshopbrandmain_abclick2shop_NA&gclid=CjwKCAjwoIqhBhAGEiwArXT7K0lUV85pMrG6sJGVX7q_JmHsOexz1Sfid1mj4Qs_hBYg2qIGRGeh1BoCH8IQAvD_BwE'

#make it later headless
options = Options()
options.headless = True
driver = webdriver.Chrome(executable_path=r'C:\Users\dionn\Thodoris\Go_Project\Python web scraping\chromedriver.exe', options=options)
driver.get(url)
time.sleep(5) #load page for sure
#use soup
html = driver.page_source
soup = BeautifulSoup(html,features="html.parser")
aElements = soup.find_all('a',href=True, class_=['sc-bg1agw-1', 'fsOPpl'] )
links = [elem['href'] for elem in aElements]
names = [elem.find('span', class_=['sc-bg1agw-2', 'fxqGXK']).text for elem in aElements]
print(len(links))
print(len(names))
#stages = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'sc-bg1agw-1') and contains(@class, 'fsOPpl')]")))
#stages = driver.find_elements(By.XPATH, "//a[contains(@class, 'sc-bg1agw-1') and contains(@class, 'fsOPpl')]")
#links = [elem.get_attribute('href') for elem in stages]

teliko = {}
for i in range(len(links)):
    teliko[names[i]] = links[i]
print(teliko)

df = pd.DataFrame()
df1 = pd.DataFrame(columns=['Name', 'Price', 'Url'])
for i in teliko:
    df = findProducts("https://www.ab.gr" + teliko[i])
    df1 = df1.append(df)
    #break

driver.close()
#print(df)
#df1 = df1.append(df)
df1.to_csv("ab.csv", sep='\t', encoding='utf-8')
#print(df1)