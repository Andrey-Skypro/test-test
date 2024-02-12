from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By 

# Устанавливаем драйвер Chrome и открываем страницу
chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
chrome_driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# Кликаем на кнопку Add Element 5 раз
for i in range(5):
    add_button = chrome_driver.find_element(By.XPATH, "//button[contains(text(), 'Add Element')]")
    add_button.click()

# Собираем список кнопок Delete
delete_buttons = chrome_driver.find_elements(By.XPATH, "//button[contains(text(), 'Delete')]")
# Выводим размер списка кнопок Delete
print(f"Size of delete buttons list in Chrome: {len(delete_buttons)}")

sleep(5) # Чтобы страница успела отобразиться перед закрытием
chrome_driver.quit()

# Устанавливаем драйвер Firefox и открываем страницу
firefox_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
firefox_driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# Кликаем на кнопку Add Element 5 раз
for i in range(5):
    add_button = firefox_driver.find_element(By.XPATH, "//button[contains(text(), 'Add Element')]")
    add_button.click()

# Собираем список кнопок Delete
delete_buttons = firefox_driver.find_elements(By.XPATH, "//button[contains(text(), 'Delete')]")
# Выводим размер списка кнопок Delete
print(f"Size of delete buttons list in Firefox: {len(delete_buttons)}")

sleep(5) # Чтобы страница успела отобразиться перед закрытием
firefox_driver.quit()




