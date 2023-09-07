from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager



"""Selenium python Script with headless Chrome"""
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# add implicit wait
driver.implicitly_wait(5)
# to maximize the browser window
driver.maximize_window()
# to refresh browser
driver.refresh()



driver.get("https://wishbox2.vercel.app/")
# search = driver.find_element(by=By.XPATH,value="//input[@placeholder='1 (702) 123-4567']")
# search.send_keys("918904098496")
# search.send_keys(Keys.RETURN)
print(driver.title)
sleep(5)
# driver.close()
driver.quit()