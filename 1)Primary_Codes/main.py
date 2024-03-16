from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")  # This line is optional, depending on your system configuration
chrome_options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"  # Update this path

driver = webdriver.Chrome(options=chrome_options)
base_url = "https://play1.automationcamp.ir/"
#driver.get("https://www.google.com")
#search_field = driver.find_element('name', 'q')
#search_field.send_keys("keep it simple stupid")
#search_field.send_keys(Keys.RETURN)  # Use Keys.RETURN to send the Enter key

driver.get(f"{base_url}/forms.html")
driver.find_element('id', 'check_python').click()
check1 = driver.find_element('id', 'check_validate').text
assert check1 == 'PYTHON'
text1 = "Hello automation world!"
driver.find_element('id','notes').send_keys(text1)
check2 = driver.find_element('id', 'area_notes_validate').text
assert check2 == text1

# Add a pause at the end of the script
input("Press Enter to close the browser...")