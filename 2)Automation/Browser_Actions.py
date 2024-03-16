from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from time import sleep

# Use ChromeOptions to configure the browser
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")  # This line is optional, depending on your system configuration

# Use ChromeDriverManager to automatically download and install Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

#  Browser Action 1 > Open Web
driver.get("https://google.com")
#sleep(1)
#  Browser Action 2 > Title Web
#Window_title = driver.title
#print(Window_title)
#  Browser Action 3 > Back
#driver.get("http://wikipedia.com")
#sleep(1)
#driver.back()
#sleep(1)
#  Browser Action 4 > Forward
#driver.forward()
#sleep(1)
#  Browser Action 5 > Refresh
#driver.refresh()

#  Browser Action 6 > Open new window  and switch to it (Tab)
#driver.switch_to.new_window('tab')

#  Browser Action 7 > Open new window  and switch to it(Window)
# driver.switch_to.new_window('window')
# driver.get("http://yahoo.com")
#a = driver.title
#print(a)
# sleep(3)
#  Browser Action 8 > Current Window
# yahoo_window = driver.current_window_handle
# print('yahoo handle'+ str(yahoo_window))
#  Browser Action 9 > All handles
# all_handle = driver.window_handles
# print('all_handles' + str(all_handle))
#  Browser Action 10 > Stitch
# driver.switch_to.window(all_handle[0])
# a = driver.title
# print(a)
# search_field = driver.find_element('name', 'q')
# search_field.send_keys("wikipedia")
# sleep(3)


#  Browser Action 11 > Close  tab
# driver.close()
# sleep(1)
#  Browser Action 12 > Quit  tab
# driver.quit()

#  Browser Action 13 > Window Size
window_size = driver.get_window_size()
print(window_size)
width = window_size['width']
print("width:", width)
height = window_size['height']
print("height:", height)
#  Browser Action 14 > Set Window Size
driver.set_window_size(800,600)
sleep(1)
size =  driver.get_window_size()
assert size['width'] == 800
print(size)

#  Browser Action 15 > Get Window Position
current_position = driver.get_window_position()
print(current_position)
sleep(1)

#  Browser Action 16 > Set Window Position
driver.set_window_position(400,500)
sleep(1)
#assert driver.get_window_position()['x']==400
# current_position = driver.get_window_position()
# print(current_position)


#  Browser Action 17 > Minimize Window
driver.minimize_window()
sleep(3)
#  Browser Action 18 > Maximize Window
driver.maximize_window()
sleep(3)

#  Browser Action 19 > Full Screen Window
driver.fullscreen_window()
sleep(3)



