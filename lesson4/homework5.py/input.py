from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# Функция для ввода и очистки поля
def enter_input_text():
    driver = webdriver.Chrome()
    driver.get("http://the-internet.herokuapp.com/inputs")

    # Вводим текст 1000 в поле
    input_field = driver.find_element(By.TAG_NAME, "input")
    input_field.send_keys("1000")
    sleep(2)  # Ждем 2 секунды

    # Очищаем поле
    input_field.clear()
    sleep(2)  # Ждем 2 секунды

    # Вводим текст 999 в поле
    input_field.send_keys("999")
    sleep(2)  # Ждем 2 секунды

    driver.quit()

enter_input_text()
print("Скрипт успешно выполнен")
