from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Python39\\resource\\chromedriver.exe")
base_ulr = "https://www.saucedemo.com/"
driver.get(base_ulr)
driver.maximize_window()

login_standart_user = "standard_user"
password_all = "secret_sauce"

user_name = driver.find_element(By.XPATH,"//input[@id='user-name']")
user_name.send_keys(login_standart_user)
print("input Login")

password = driver.find_element(By.XPATH,"//input[@id='password']")
password.send_keys(password_all)
print("input Password")
password.send_keys(Keys.RETURN)

filter = driver.find_element(By.XPATH,"//select[@data-test='product_sort_container']")
filter.click()
print("Click Filter")
filter.send_keys(Keys.DOWN)
filter.send_keys(Keys.RETURN)
