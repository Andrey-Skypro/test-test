from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

# Функция для клика на кнопку с динамическим идентификатором
def click_dynamic_id_button(driver):
    driver.get("http://uitestingplayground.com/dynamicid")
    # Поиск кнопки по тексту
    dynamic_id_button = driver.find_element(By.XPATH, "//button[contains(text(),'Button with Dynamic ID')]")
    dynamic_id_button.click()

# Устанавливаем драйвер Chrome и вызываем функцию
chrome_driver = webdriver.Chrome()
for _ in range(3):
    click_dynamic_id_button(chrome_driver)
    sleep(3)  # Ждем немного между запусками чтобы страница успела обновиться

chrome_driver.quit()

# Устанавливаем драйвер Firefox и вызываем функцию
firefox_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
for _ in range(3):
    click_dynamic_id_button(firefox_driver)
    sleep(3)  # Ждем немного между запусками чтобы страница успела обновиться

firefox_driver.quit()

print("Скрипт успешно выполнен")
