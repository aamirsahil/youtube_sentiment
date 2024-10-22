from selenium import webdriver
from selenium.webdriver.common.by import By
import os

# os.environ['PATH'] += r"D:/SeleniumDrivers"
driver = webdriver.Chrome()
driver.get('https://www.seleniumeasy.com/test/jquery-download-progress-bar-demo.html')
driver.implicitly_wait(10)
downlaod_button = driver.find_element(By.ID, "")