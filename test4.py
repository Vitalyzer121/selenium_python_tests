import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\Python39\\Project\\SeleniumProject\\chromedriver.exe")
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
button_login = driver.find_element(By.XPATH,"//input[@id='login-button']")
button_login.click()
print("Click Login Button")

#driver.execute_script('window.scrollTo(0, 500)')
action = ActionChains(driver)
red_t_shirt = driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-onesie']")
action.move_to_element(red_t_shirt).perform()

now_date = datetime.datetime.utcnow().strftime('%Y.%m.%d.%H.%M.%S')
name_screenshot = 'screenshot' + now_date + '.png'
driver.save_screenshot('C:\\Python39\\SeleniumProject\\Screen\\' + name_screenshot)