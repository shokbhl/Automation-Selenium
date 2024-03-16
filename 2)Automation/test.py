from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from time import sleep
import os
from pathlib import Path


# Use ChromeOptions to configure the browser
chrome_options = Options()
#chrome_options.add_argument("--no-sandbox")  # This line is optional, depending on your system configuration
chrome_options.add_argument("--incognito")  # This line is optional, depending on your
#chrome_options.add_argument("--headless")  # This line is optional, depending on your
# Use ChromeDriverManager to automatically download and install Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("http://yahoo.com")
sleep(3)
driver.find_element('id', 'ybar-sbq')
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(2)
current_path = Path(__file__).parent
file_name = os.path.join(str(current_path), 'session2.png')
driver.save_screenshot(file_name)

