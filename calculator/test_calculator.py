from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("http://localhost:8082")

numbers = driver.find_elements(By.TAG_NAME, "input")

numbers[0].send_keys("10")
numbers[1].send_keys("5")

buttons = driver.find_elements(By.TAG_NAME, "button")
buttons[0].click()

time.sleep(2)

result = driver.find_element(By.ID, "result").text

print("Test Result:", result)

assert "15" in result

print("Calculator Test Passed!")

driver.quit()