import os 
import logging
import pickle
import config
import time
from termcolor import colored 
from tkinter import Y
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import logging
import json
import bs4
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from twilio.rest import Client

#from config import DispatchToTelegram, ExPositions, ExtractName, ExtractSoup, HandlePosition, Load_Pickle,  pickle_it, telegram_bot_sendtext

#tradinghorse


URL = 'https://candidature.1337.ma/piscines'

headers = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}

def main(url,new_position = True):
    page = requests.get(URL , headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    user = "yassine1337idrissi@gmail.com"
    password = "Yassin@0661535096"
    
    
    driver = webdriver.Chrome('/home/yassin_chati_98/1337/boot_cloud/chromedriver')
    driver.get(URL)

    driver.find_element_by_id("user_email").send_keys(user)
    time.sleep(2)
    driver.find_element_by_id("user_password").send_keys(password)
    time.sleep(1)
    driver.find_element_by_name("commit").click()
    time.sleep(2)
    url2 = "https://candidature.1337.ma/piscines"
    page2 = requests.get(url2 , headers=headers)
    soup2 = BeautifulSoup(page2.content, "html.parser")
    # print(soup2)
    # driver.find_element_by_class_name("recaptcha-checkbox-borderAnimation").click()
    # *tihs 👆🏻 is for click on non-human touch device

    x = 0
    y = 0
    if soup != soup2:
        config.telegram_bot_sendtext_t("🚀ana an9l3🚀")
        print("I m insade the web site")
    while True:
        driver.refresh()
        page3 = requests.get(url2 , headers=headers)
        soup3 = BeautifulSoup(page2.content, "html.parser")
        if soup3 != soup2:
            print("there is a new piscine")
            config.telegram_bot_sms("🚨kayn piscine-pooooooooool🚨 🔗ha lien: https://candidature.1337.ma/piscines🔗 🏃‍♂️ serbi chdo 🏃‍♂️", ayoub)
            config.telegram_bot_sms("🚨kayn piscine-pooooooooool🚨 🔗ha lien: https://candidature.1337.ma/piscines🔗 🏃‍♂️ serbi chdo 🏃‍♂️", khalid)
            config.telegram_bot_sendtext("🚨kayn piscine-pooooooooool🚨")
            config.telegram_bot_sendtext("🔗ha lien: https://candidature.1337.ma/piscines🔗")
            config.telegram_bot_sendtext("🏃‍♂️ serbi chdo 🏃‍♂️")
            config.elegram_bot_call()
            time.sleep(20)
            config.telegram_bot_call_a()
            time.sleep(20)
            config.telegram_bot_call_k()
            exit()
        else:
            x +=1
            y +=1
            if x > 15:
                print ("i try ",y,"times but no pool😥")
                config.telegram_bot_sendtext_t("😋gha thna rah mzl matla7 pool😉")
                x = 0      
            # exit()
                # telegram_bot_sendtext("🙏 sorry, just a test🙏")
        time.sleep(20)
    driver.quit()

        
if __name__ == "__main__":
    try:
        main()
    except TimeoutException :
        time.sleep(500)
        main()