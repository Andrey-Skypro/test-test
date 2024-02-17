from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# Функция для авторизации
def login():
    driver = webdriver.Chrome()
    driver.get("http://the-internet.herokuapp.com/login")

    # Вводим имя пользователя и пароль
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("tomsmith")
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")
    
    # Нажимаем кнопку Login
    login_button = driver.find_element(By.CSS_SELECTOR, "[type='submit']")
    login_button.click()

    sleep(2)  # Ждем 2 секунды

    # Проверяем, что успешно залогинились
    success_message = driver.find_element(By.ID, "flash").text
    if "You logged into a secure area!" in success_message:
        print("Успешно вошли в систему.")
    else:
        print("Не удалось войти в систему.")

    driver.quit()

login()
