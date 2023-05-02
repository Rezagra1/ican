from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("http://10.116.7.155/FarzinSoft/eOrgan/Login/LoginFrm.aspx?Rnd=11:04:02%20AM&GSN=1")

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, "Loginbtn")))

username_field = driver.find_element(By.ID, "UserName")
username_field.send_keys("ican2")

password_field = driver.find_element(By.ID, "Password")
password_field.send_keys("963852741")

loigin_buttom = driver.find_element(By.ID, "Loginbtn")
loigin_buttom.click()
time.sleep(10)


setting_btm = driver.find_element(By.CLASS_NAME,"div.btn.btn-link.btn-sm[name='كاربران']")
setting_btm.click()


time.sleep(50000)
print("done")
