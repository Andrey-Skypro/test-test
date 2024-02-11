from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# Функция для клика на кнопку с динамическим идентификатором
def click_dynamic_id_button():
    driver = webdriver.Chrome()
    driver.get("http://uitestingplayground.com/dynamicid")
    # Поиск кнопки по тексту
    dynamic_id_button = driver.find_element(By.XPATH, "//button[contains(text(),'Button with Dynamic ID')]")
    dynamic_id_button.click()
    driver.quit()

# Запускаем скрипт 3 раза
for _ in range(3):
    click_dynamic_id_button()
    sleep(3)  # Ждем немного между запусками чтобы страница успела обновиться

print("Скрипт успешно выполнен")


