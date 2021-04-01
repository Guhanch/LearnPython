import datetime
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import pywhatkit
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=D:\Python\Memory\WebWhatsAppBot")

driver = webdriver.Chrome(executable_path='C:\\Program Files\\chromedriver_win32\\chromedriver.exe',options=options)
print(datetime.datetime.now())
driver.get('https://www.goodreturns.in/gold-rates/chennai.html')
print(datetime.datetime.now())
v = datetime.datetime.now()
dates = datetime.datetime.strftime(v,'%d-%m-%Y')
driver.maximize_window()
header = driver.find_element_by_xpath('//*[@id="moneyweb-leftPanel"]/div[5]/h2').text
print(header)
one_g = ' One Gram: '
one_g += driver.find_element_by_xpath('//*[@id="moneyweb-leftPanel"]/div[6]/table/tbody/tr[2]/td[2]').text + '\n'
eight_g = ' Eight Gram: '
eight_g += driver.find_element_by_xpath('//*[@id="moneyweb-leftPanel"]/div[6]/table/tbody/tr[3]/td[2]').text + '\n'
price_diff= 'Price Difference per gram from Yesterday: '
price_diff+= driver.find_element_by_xpath('//*[@id="moneyweb-leftPanel"]/div[6]/table/tbody/tr[2]/td[4]/span').text
today_rate = [dates,one_g,eight_g,price_diff]
print(today_rate)
driver.get('https://web.whatsapp.com')
time.sleep(20)
phone_num = ['Balakrishnan Mama','Ponds','Aruna']

for i in range(len(phone_num)):
    search_w = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    driver.execute_script("arguments[0].click();", search_w)
    time.sleep(3)
    search_w.send_keys(phone_num[i]+ Keys.ENTER)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys("Automated Web Message\n "+"Today 22 Carat Gold Price \n ")
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(today_rate)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span').click()

driver.quit()

# pywhatkit.sendwhatmsg('+916380546245','test_sucess',16,40)
