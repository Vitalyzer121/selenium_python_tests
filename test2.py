from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Python39\\resource\\chromedriver.exe")
base_ulr = "https://www.saucedemo.com/"
driver.get(base_ulr)
driver.maximize_window()

login_standart_user = "standard_use"
password_all = "secret_sauce"

user_name = driver.find_element(By.XPATH,"//input[@id='user-name']")
user_name.send_keys(login_standart_user)
print("input Login")
password = driver.find_element(By.XPATH,"//input[@id='password']")
password.send_keys(password_all)
print("input Password")
button_login = driver.find_element(By.XPATH,"//input[@id='login-button']")
button_login.click()
print("Click Login Button")

warring_text = driver.find_element(By.XPATH,"//h3[@data-test ='error']")
value_warring_text = warring_text.text
assert value_warring_text == "Epic sadface: Username and password do not match any user in this service"
print("Good Test")

driver.refresh()
