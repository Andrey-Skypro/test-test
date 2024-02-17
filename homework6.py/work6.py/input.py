from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")

try:
    input_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "text"))
    )
    
    input_field.send_keys("SkyPro")
    
    button = driver.find_element(By.ID, "testbutton")
    button.click()
    
    time.sleep(2)
    
    button_text = driver.find_element(By.ID, "demotext").text
    
    print(button_text)

except TimeoutException:
    print("Timeout waiting for element to be located")

driver.quit()

