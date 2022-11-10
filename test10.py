import datetime
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\Python39\\SeleniumProject\\chromedriver.exe")
base_ulr = "https://demoqa.com/dynamic-properties"
driver.get(base_ulr)
#driver.maximize_window()
#driver.implicitly_wait(10)

#print("Start Test")
#visible_button = driver.find_element(By.XPATH,"//button[@id='visibleAfter']")
#visible_button.click()
#print("Finish Test")

print("Start Test")
visible_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,"//button[@id='visibleAfter']")))
visible_button.click()
print("Finish Test")



