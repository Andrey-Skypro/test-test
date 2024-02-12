from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# Функция для клика на кнопку с CSS-классом и обработки всплывающего алерта
def click_blue_button(driver):
    driver.get("http://uitestingplayground.com/classattr")
    blue_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
    blue_button.click()
    
    try:
        alert = driver.switch_to.alert
        print(f"Alert Text: {alert.text}")
        alert.accept()
    except:
        pass

# Устанавливаем драйвер Chrome и вызываем функцию
chrome_driver = webdriver.Chrome()
for _ in range(3):
    click_blue_button(chrome_driver)
    sleep(3)

chrome_driver.quit()

# Устанавливаем драйвер Firefox и вызываем функцию
firefox_driver = webdriver.Firefox()
for _ in range(3):
    click_blue_button(firefox_driver)
    sleep(3)

firefox_driver.quit()

print("Скрипт успешно выполнен")

