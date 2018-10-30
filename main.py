from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome()



driver.get("https://www.google.com/")

search_bar = driver.find_element_by_id("lst-ib")
search_bar.send_keys("search this")
search_bar.send_keys(Keys.ENTER)


