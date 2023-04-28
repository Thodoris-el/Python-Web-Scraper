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


def findProducts(url):
    df = pd.DataFrame(columns=['Name', 'Price', 'Url'])
    count = 0
    flag = False
    while True:
        print(url + "?pageNumber=" + str(count))
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(executable_path=r'C:\Users\dionn\Thodoris\Go_Project\Python web scraping\chromedriver.exe', options=options)
        try:
            driver.get(url + "?pageNumber=" + str(count)) 
            time.sleep(5)
        except:
            print("test")
            break
        #stages = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'sc-y4jrw3-6') and contains(@class, 'jSkhQP')]")))
        #stages = driver.find_elements(By.XPATH, "//a[contains(@class, 'sc-y4jrw3-6') and contains(@class, 'jSkhQP')]")
        html = driver.page_source
        soup = BeautifulSoup(html,features="html.parser")
        #print(soup)
        #a = soup.find_all("a", {"class": "sc-1qeaiy2-2 jRcVhP"})
        #a = soup.find_all('a',href=True, class_=['sc-y4jrw3-6', 'jSkhQP'] )
        #links = [elem['href'] for elem in a]
        #print(a[0]['aria-label'])
        #exit()

        #Get li of each product
        listOfProducts = soup.find_all("li", class_=["sc-3brks3-4", "eRw", "product-item"])
        if listOfProducts == []:
            break
        links = [elem.find("a", {"class": "sc-y4jrw3-6 jSkhQP"})['href'] for elem in listOfProducts]
        names = [elem.find("a", {"class": "sc-y4jrw3-6 jSkhQP"})['aria-label'] for elem in listOfProducts]
        price = [elem.find("div", attrs={"data-testid":["product-block-price", "product-block-unavailable-text"]}).text for elem in listOfProducts]
        #price = [elem.find("div", class_= ["sc-1qeaiy2-2", "oTDWG"]).text for elem in listOfProducts]
        #print(links[0], price[0], names[0])
        teliko = {}
        for i in range(len(links)):
            df = df.append({'Name' : names[i], 'Price' : price[i], 'Url' : links[i]}, ignore_index = True)
        count = count + 1
        
        '''
        for i in teliko:
            break
            print(i)
            driver.get(i)
            try:
                prod = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'sc-1qeaiy2-2') and contains(@class, 'jRcVhP')]")))
                prodPrice = driver.find_element(By.XPATH, "//div[contains(@class, 'sc-1qeaiy2-2') and contains(@class, 'jRcVhP')]")
                print(prodPrice.text)
            except:
                print("no price found")
        '''

        
    driver.close()
    print(df)
    return df
