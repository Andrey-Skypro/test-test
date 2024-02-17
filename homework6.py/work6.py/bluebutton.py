from selenium import webdriver
import time
from selenium.webdriver.common.by import By 

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/ajax")

button = driver.find_element(By.ID,("ajaxButton"))
button.click()

time.sleep(2)

green_text = driver.find_element(By.ID,("p4")).text

print(green_text)

driver.quit()
