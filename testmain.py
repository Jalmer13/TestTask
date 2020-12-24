import time
import pyautogui as pag
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color

browser = webdriver.Chrome()
browser.get('https://netpeak.ua/')

xpath1 = '/html/body/header/div[2]/div/div/div[2]/div/nav/ul/li[5]/a'
button = browser.find_element_by_xpath(xpath1).click()

xpath2 = '/html/body/div[5]/div/div/div[5]/div/a'
button = browser.find_element_by_xpath(xpath2).click()

xpath3 = '/html/body/form/div[1]/div/div[1]/div[8]/div[1]/div[3]/button'
button = browser.find_element_by_xpath(xpath3).click()

time.sleep(2)

pag.typewrite('https://images.netpeak.ua/logos/logo%20netpeak_2020_full_white.png')

pag.press('enter')

time.sleep(3)

assert "Ошибка: неверный формат файла" in browser.page_source

browser.find_element_by_xpath('/html/body/form/div[1]/div/div[1]/div[10]/div[1]/div[1]/input').send_keys('Vasya')
browser.find_element_by_xpath('/html/body/form/div[1]/div/div[1]/div[10]/div[1]/div[2]/input').send_keys('Vasiliev')
browser.find_element_by_xpath('/html/body/form/div[1]/div/div[1]/div[10]/div[2]/input').send_keys('Vasya@Vasya.vas')
browser.find_element_by_xpath('/html/body/form/div[1]/div/div[1]/div[11]/div[5]/input').send_keys('+1234567890')

button = browser.find_element_by_xpath('/html/body/form/div[1]/div/div[1]/div[11]/div[2]/select').click()
button = browser.find_element_by_xpath('/html/body/form/div[1]/div/div[1]/div[11]/div[2]/select/option[13]').click()

button = browser.find_element_by_xpath('/html/body/form/div[1]/div/div[1]/div[11]/div[3]/select').click()
button = browser.find_element_by_xpath('/html/body/form/div[1]/div/div[1]/div[11]/div[3]/select/option[8]').click()

button = browser.find_element_by_xpath('/html/body/form/div[1]/div/div[1]/div[11]/div[4]/select').click()
button = browser.find_element_by_xpath('/html/body/form/div[1]/div/div[1]/div[11]/div[4]/select/option[14]').click()

button = browser.find_element_by_xpath('/html/body/form/div[2]/button').click()

time.sleep(2)

Color.from_string(browser.find_element(By.XPATH,'/html/body/div[2]/div/p').value_of_css_property('color'))
print(browser.find_element(By.XPATH,'/html/body/div[2]/div/p').value_of_css_property('color'))

button = browser.find_element_by_xpath('/html/body/header/div[2]/div/div/div[2]/div/nav/ul/li[4]/a').click()

browser.current_url
print(browser.current_url)

time.sleep(5)

browser.quit()
