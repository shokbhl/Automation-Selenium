from logintest.Pages.login import Login
from selenium import webdriver
from logintest.Pages.MainPage import MainPage
from time import sleep
import unittest

class LoginTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.ChromeOptions()
        cls.driver.add_argument("--no-sandbox")  # This line is optional, depending on your system configuration
        cls.driver.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"  # Update this path
        cls.driver = webdriver.Chrome(options=cls.driver)
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()

    def test_valid_login(self):
        self.driver.get("https://www.saucedemo.com/")
        login =Login(driver= self.driver)
        main_page = MainPage(driver = self.driver)
        login.enter_username("standard_user")
        login.enter_password("secret_sauce")
        login.click_on_login_button()
        main_page.check_main_page()
        sleep(1)
        pass

    def test_invalid_login(self):
        self.driver.get("https://www.saucedemo.com/")
        login = Login(driver=self.driver)
        main_page = MainPage(driver=self.driver)
        login.enter_username("standard_user")
        login.enter_password("secret_saucet")
        login.click_on_login_button()
        main_page.check_main_page()
        sleep(1)
        pass

if __name__ == '__main__':
    unittest.main()
