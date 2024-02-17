from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# Функция для клика на кнопку с CSS-классом
def click_blue_button():
    driver = webdriver.Chrome()
    driver.get("http://uitestingplayground.com/classattr")
    blue_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
    blue_button.click()
    driver.quit()

# Запускаем скрипт 3 раза
for _ in range(3):
    click_blue_button()
    sleep(3)  # Ждем немного между запусками чтобы страница успела обновиться

print("Скрипт успешно выполнен")

