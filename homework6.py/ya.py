from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

#browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser.get("https://ya.ru")
browser.get("https://google.com")
browser.back()
sleep(15)