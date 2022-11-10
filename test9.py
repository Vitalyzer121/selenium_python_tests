import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\Python39\\SeleniumProject\\chromedriver.exe")
base_ulr = "http://automationpractice.com/index.php?id_category=3&controller=category"
driver.get(base_ulr)
driver.maximize_window()

action = ActionChains(driver)

price = driver.find_element(By.XPATH,"//div[@id='layered_price_slider']")
action.click_and_hold(price).move_by_offset(20,0).release().perform()
print("Price +")





