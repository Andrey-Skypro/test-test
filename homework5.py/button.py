
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 

# Устанавливаем драйвер и открываем страницу
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# Кликаем на кнопку Add Element 5 раз
for i in range(5):
    add_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Add Element')]")
    add_button.click()

# Собираем список кнопок Delete
delete_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Delete')]")

# Выводим размер списка кнопок Delete
print(f"Размер списка кнопок Delete: {len(delete_buttons)}")

sleep(15) # Чтобы страница успела отобразиться перед закрытием

driver.quit()