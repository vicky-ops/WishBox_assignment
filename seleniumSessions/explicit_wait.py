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

# Find the search bar by namme
search_bar = driver.find_element(By.NAME, 'q')

# Enter a search term
search_bar.send_keys("Selenium")


#find search button
search_bth = driver.find_element(By.NAME,'btnK')
search_bar.click()

# Wait for the search results to load
WebDriverWait(driver,10).until(EC.presence_of_element_located(By.ID,""))

# Get all the search results
search_results = driver.find_elements(By.XPATH,"//div[@class='g']")

# loop through the search results
for search_result in search_results:
    # Get the href of the search result
    href = search_result.find_element(By.XPATH,".//a").get_attribute("href")

    # Check if the href contains the text 'https://selenium.dev'
    if "https://www.selenium.dev/" in href:
        print(f"Found the search result: {href}")

driver.quit()








driver.quit()