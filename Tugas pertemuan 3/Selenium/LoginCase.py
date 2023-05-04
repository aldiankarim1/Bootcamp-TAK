import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObject.locator import elem
from PageObject.data import data, title
import login
import time


class Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_login(self):
        driver = self.driver
        login.testLogin(driver, data.email, data.password)
        url = driver.current_url
        self.assertEqual(url, data.baseURL)
        welcome = driver.find_element(
            By.CLASS_NAME, elem.welcome).text
        self.assertEqual(welcome, title.title_welcome)
        welcome1 = driver.find_element(
            By.XPATH, elem.welcome1).text
        self.assertEqual(welcome1, title.title_welcome1)
        welcome2 = driver.find_element(
            By.XPATH, elem.welcome2).text
        self.assertEqual(welcome2, title.title_welcome2)
        featured = driver.find_element(By.XPATH, elem.title_featured).text
        self.assertEqual(featured, title.title_featured)

    def test_login_email_blank(self):
        driver = self.driver
        login.testLogin(driver, data.emailBlank, data.password)
        url = driver.current_url
        self.assertEqual(url, data.baseURL + "login")
        msg_login_email_blank = driver.find_element(
            By.XPATH, elem.msg_login_email_blank).text
        self.assertEqual(msg_login_email_blank,
                         data.msg_login_email_blank)
        msg_login_email_blank_1 = driver.find_element(
            By.XPATH, elem.msg_login_email_blank_1).text
        self.assertEqual(msg_login_email_blank_1,
                         data.msg_login_email_blank_1)

    def test_login_password_blank(self):
        driver = self.driver
        login.testLogin(driver, data.emailBlank, data.password)
        url = driver.current_url
        self.assertEqual(url, data.baseURL + "login")
        msg_login_password_blank = driver.find_element(
            By.XPATH, elem.msg_login_password_blank).text
        self.assertEqual(msg_login_password_blank,
                         data.msg_login_email_blank_1)
        msg_login_email_blank = driver.find_element(
            By.XPATH, elem.msg_login_email_blank).text
        self.assertEqual(msg_login_email_blank,
                         data.msg_login_email_blank)

    def test_login_format_email_invalid(self):
        driver = self.driver
        login.testLogin(driver, data.emailInvalid, data.password)
        url = driver.current_url
        self.assertEqual(url, data.baseURL + "login")
        msg_invalid_format_email = driver.find_element(
            By.XPATH, elem.msg_invalid_format_email).text
        self.assertEqual(msg_invalid_format_email,
                         data.msg_invalid_format_email)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
