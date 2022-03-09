
# from re import X
# from tkinter import Y
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

URL = 'https://candidature.1337.ma/piscines'
ana = '+212682392135'
ayoub = '+212615252254'
khalid = '+212655456084'


def telegram_bot_sendtext(bot_message):
    bot_token = "5133253099:AAG-g5TgU-zZtKP8HEUaLqWXkMRcz8Slm6I"
    bot_chatID = '-1001536466676'
    send_text = 'https://api.telegram.org/bot' + bot_token + \
        '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()

def telegram_bot_sendtext_t(bot_message):
    bot_token = "5208425825:AAFYqnvNJkfVkQ1-45twV2qJ8alQj_BL0rU"
    bot_chatID = '-1001623813461'
    send_text = 'https://api.telegram.org/bot' + bot_token + \
        '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()

def telegram_bot_sms(sms_message, number):
    account_sid = "ACa726c89d9f2621fd952c46fd3cad2354" 
    auth_token = "fdb8f89f298cf1d60b27527134064510"
    client = Client(account_sid, auth_token)

    message = client.messages \
    .create(
         body= sms_message,
         from_='+19808907222',
         to= number
     )

    print(message.sid)



def telegram_bot_call():
    account_sid = "ACa726c89d9f2621fd952c46fd3cad2354"
    auth_token = "fdb8f89f298cf1d60b27527134064510"
    client = Client(account_sid, auth_token)
    call = client.calls.create(
                        twiml='<Response><Say voice="rah kayn piscine db. srbi asahbi!</Say><Play>http://demo.twilio.com/docs/classic.mp3</Play></Response>',
                        to='+212682392135',
                        from_='+19808907222'
                     )

    print(call.sid)

def telegram_bot_call_a():
    account_sid = "ACa726c89d9f2621fd952c46fd3cad2354"
    auth_token = "fdb8f89f298cf1d60b27527134064510"
    client = Client(account_sid, auth_token)
    call = client.calls.create(
                        twiml='<Response><Say voice="rah kayn piscine db. srbi asahbi!</Say><Play>http://demo.twilio.com/docs/classic.mp3</Play></Response>',
                        to='+212615252254',
                        from_='+19808907222'
                     )

    print(call.sid)

def telegram_bot_call_k():
    account_sid = "ACa726c89d9f2621fd952c46fd3cad2354"
    auth_token = "fdb8f89f298cf1d60b27527134064510"
    client = Client(account_sid, auth_token)
    call = client.calls.create(
                        twiml='<Response><Say voice="rah kayn piscine db. srbi asahbi!</Say><Play>http://demo.twilio.com/docs/classic.mp3</Play></Response>',
                        to='+212655456084',
                        from_='+19808907222'
                     )

chrome_options = Options()
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome('/home/yassin_chati_98/1337/boot_cloud/chromedriver', options=options)
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

headers = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}
page = requests.get(URL , headers=headers)
soup = BeautifulSoup(page.content, "html.parser")

user = "yassine1337idrissi@gmail.com"
password = "Yassin@0661535096"

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

# x = 0
# y = 0
# if soup != soup2:
#     telegram_bot_sendtext_t("🚀ana an9l3🚀")
#     print("I m insade the web site")
# while True:
#     driver.refresh()
#     page3 = requests.get(url2 , headers=headers)
#     soup3 = BeautifulSoup(page2.content, "html.parser")
#     if soup3 != soup2:
#         print("there is a new piscine")
#         telegram_bot_sms("🚨kayn piscine-pooooooooool🚨 🔗ha lien: https://candidature.1337.ma/piscines🔗 🏃‍♂️ serbi chdo 🏃‍♂️", ayoub)
#         telegram_bot_sms("🚨kayn piscine-pooooooooool🚨 🔗ha lien: https://candidature.1337.ma/piscines🔗 🏃‍♂️ serbi chdo 🏃‍♂️", khalid)
#         telegram_bot_sms("🚨kayn piscine-pooooooooool🚨 🔗ha lien: https://candidature.1337.ma/piscines🔗 🏃‍♂️ serbi chdo 🏃‍♂️", ana)
#         telegram_bot_sendtext("🚨kayn piscine-pooooooooool🚨")
#         telegram_bot_sendtext("🔗ha lien: https://candidature.1337.ma/piscines🔗")
#         telegram_bot_sendtext("🏃‍♂️ serbi chdo 🏃‍♂️")
#         telegram_bot_call()
#         time.sleep(20)
#         telegram_bot_call_a()
#         time.sleep(20)
#         telegram_bot_call_k()
#         exit()
#     else:
#         x +=1
#         y +=1
#         if x > 15:
#             print ("i try ",y,"times but no pool😥")
#             telegram_bot_sendtext_t("😋gha thna rah mzl matla7 pool😉")
#             x = 0      
#         # exit()
#             # telegram_bot_sendtext("🙏 sorry, just a test🙏")
#     time.sleep(20)

# driver.close()
#! the code stop here 🙏


# headers = {
# "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36"
# }
# # page = requests.get(URL, headers=headers)
# # time.sleep(5)

# # soup = BeautifulSoup(page.content, 'html.parser')
# # print(soup)

# # print(soup)
# user = "yassine1337idrissi@gmail.com"
# password = "Yassin@0661535096"

# driver.get(URL)
# print(driver.text())
# username_login = driver.find_element_by_id("string email optional")
# password_login = driver.find_element_by_class_name("password optional")
# # username_login.send_keys(user)
# # time.sleep(1)
# # password_login.send_keys(password)
# user = soup.find("input",{"class":"string email optional"})
# #how i will know that this code is work
# print(user)

# piscine = soup.find()
# price = soup.find(id="corePrice_desktop")

# # button = driver.find_element_by_tag_name("Sign in")
# time.sleep(2)
# button.click()
# time.sleep(2)
# soup2 = BeautifulSoup(page.content,'html.parser')
# if soup2.text != soup.text:
#     print(soup2.text)

# print(piscine)
# print(username_login)
# print(title)