import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Initialize the browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Add implicit wait
driver.implicitly_wait(2)
# Maximize the window
driver.maximize_window()
# refresh the window
driver.refresh()

driver.get("https://www.google.com")


driver.get("https://google.com")
print(driver.title)
time.sleep(3)
driver.quit()