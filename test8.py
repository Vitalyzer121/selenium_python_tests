import datetime
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(executable_path="C:\\Python39\\SeleniumProject\\chromedriver.exe")
base_ulr = "https://demoqa.com/radio-button"
driver.get(base_ulr)
driver.maximize_window()

#check_box = driver.find_element(By.XPATH,"//button[@aria-label='Toggle']")
#check_box.click()

#radio_button = driver.find_element(By.XPATH,"//label[@for='yesRadio']")
#radio_button.click()
#action = ActionChains(driver)
#double = driver.find_element(By.XPATH,"//button[@id='doubleClickBtn']")
#action.double_click(double).perform()

# = driver.find_element(By.XPATH,"//button[@id='rightClickBtn']")
#action.context_click(right_click).perform()
#try:
#    visible_button = driver.find_element(By.XPATH,"//button[@id='visibleAfter']")
#    visible_button.click()
#except NoSuchElementException as exception:
#   print("NoSuchElementException")
#   time.sleep(10)
#  visible_button = driver.find_element(By.XPATH, "//button[@id='visibleAfter']")
#   visible_button.click()
#   print("Click Visible Button")

yes_checkbox = driver.find_element(By.XPATH,"//label[@for='yesRadio']")
yes_checkbox.click()
try:
    message = driver.find_element(By.XPATH,"//span[@class='text-success']")
    value_message = message.text
    print(value_message)
    assert value_message == "No"
except AssertionError as exception:
    driver.refresh()
    yes_checkbox = driver.find_element(By.XPATH, "//label[@for='yesRadio']")
    yes_checkbox.click()
    message = driver.find_element(By.XPATH, "//span[@class='text-success']")
    value_message = message.text
    print(value_message)
    assert value_message == "Yes"
    print("Checkbox YES")
print("Test over")