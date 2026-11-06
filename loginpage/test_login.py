from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("http://localhost:5000")

username = driver.find_element(By.NAME, "username")
username.send_keys("Dharshika")

password = driver.find_element(By.NAME, "password")
password.send_keys("12345")

button = driver.find_element(By.TAG_NAME, "button")
button.click()

time.sleep(2)

result = driver.find_element(By.TAG_NAME, "body").text

print("Test Result:", result)

assert "Login Successful" in result

print("Login Test Passed!")

driver.quit()