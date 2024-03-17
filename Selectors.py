
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

# Use ChromeOptions to configure the browser
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")  # This line is optional, depending on your system configuration

# Use ChromeDriverManager to automatically download and install Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

#  Browser Action 1 > Open Web
driver.get("https://www.wikipedia.org/")

#1> ID
# el1 = driver.find_element('id', 'searchInput')
el1 = driver.find_element('css selector', '#searchInput')
el1.send_keys("Hello  world")
sleep(3)

#2> Xpath
# el2 = driver.find_element('xpath', "//input[@type='search']")
# print(el1)
# print(el2)
# assert el1 == el2

# el3 = driver.find_element('xpath', "//*[text()='Italiano']")
# el3.click()
# sleep(3)

#3>
# el4 = driver.find_element('tag name', 'select')
# el4.click()
# sleep(3)


#4> link Text
# Find and click the element using link text
# driver.find_element(By.LINK_TEXT, 'Download Wikipedia for Android or iOS').click()
# sleep(3)

#5> Partial link  Text
# driver.find_element('partial link text', 'Download').click()
# sleep(3)

#6> class name
# driver.find_element(By.CLASS_NAME, 'svg-search-icon').click()
# sleep(3)

#7> CSS
# driver.find_element('css selector', '.svg-search-icon').click()
# sleep(3)

