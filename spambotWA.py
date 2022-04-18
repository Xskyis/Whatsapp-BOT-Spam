# Importing modules/librairies
from cgitb import text
from distutils.log import info
from unicodedata import name
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

message = "Pesan Kamu"
amount = 100
delay = 0.1
contact = "Target Kamu"

Options = webdriver.ChromeOptions()
Options.add_argument('user-data-dir=D:\\ChromeProfile')

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe", chrome_options=Options)

driver.get('https://web.whatsapp.com/')
driver.minimize_window()

time.sleep(20)

name_list = []

# //*[@id="pane-side"]/div/div/div/div[7]
# //*[@id="pane-side"]/div/div/div/div[7]/div/div/div[2]/div[1]/div[1]/span

for i in range(1, 15):
    info = driver.find_element_by_xpath(f'//*[@id="pane-side"]/div/div/div/div[{i}]' + '/div/div/div[2]/div[1]/div[1]/span')
    name_list.append(info.text)

to_click = name_list.index(contact) + 1

driver.find_element_by_xpath(f'//*[@id="pane-side"]/div/div/div/div[{to_click}]').click()

time.sleep(2)

# //*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]

for i in range(amount):
    text_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
    text_box.send_keys(message)
    text_box.send_keys(Keys.ENTER)
    time.sleep(delay)

