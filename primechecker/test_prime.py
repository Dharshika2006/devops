from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("http://localhost:8081")

number = driver.find_element(By.ID, "num")
number.send_keys("7")

button = driver.find_element(By.TAG_NAME, "button")
button.click()

time.sleep(2)

result = driver.find_element(By.ID, "result").text

print("Test Result:", result)

assert "Prime" in result

print("Prime Number Test Passed!")

driver.quit()