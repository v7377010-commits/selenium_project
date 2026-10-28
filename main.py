import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

BASE_URL 'https://ya.ru'
driver = webdriver.Chrome()
driver.get(BASE_URL)

search_field = driver.find_element(By.XPATH, "//*[@name='text']")
search_field.send_keys('Вика')
search_field.send_keys(Keys.ENTER)

time.sleep(5)
driver.quit()