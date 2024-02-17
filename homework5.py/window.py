from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# Открываем страницу и закрываем модальное окно
def close_modal():
    driver = webdriver.Chrome()
    driver.get("http://the-internet.herokuapp.com/entry_ad")

    # Проверяем, что модальное окно отображается
    modal = driver.find_element(By.ID, "modal")
    if "modal" in modal.get_attribute("class"):
        # Нажимаем кнопку Close
        close_button = driver.find_element(By.CSS_SELECTOR, ".modal-footer p")
        close_button.click()

    driver.quit()

close_modal()
print("Скрипт успешно выполнен")