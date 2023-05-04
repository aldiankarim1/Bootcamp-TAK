import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObject.locator import elem
from PageObject.data import data, title
import register
import time


class Register(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_success_register(self):
        driver = self.driver
        register.register(driver, data.firstName, data.lastName,
                          data.email, data.password, data.ConfirmPassword)

    def test_failed_register_firstName_blank(self):
        driver = self.driver
        register.register(driver, data.firstNameBlank, data.lastName,
                          data.email, data.password, data.ConfirmPassword)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, elem.msg_firstName_blank)))
        msg_firstName_blank = driver.find_element(
            By.XPATH, elem.msg_firstName_blank).text
        self.assertEqual(data.msg_firstName_blank, msg_firstName_blank)

    def test_failed_register_lastName_blank(self):
        driver = self.driver
        register.register(driver, data.firstName, data.lastNameBlank,
                          data.email, data.password, data.ConfirmPassword)
        msg_lastName_blank = driver.find_element(
            By.XPATH, elem.msg_lastName_blank).text
        self.assertEqual(data.msg_lastName_blank, msg_lastName_blank)

    def test_failed_register_email_blank(self):
        driver = self.driver
        register.register(driver, data.firstName, data.lastName,
                          data.emailBlank, data.password, data.ConfirmPassword)
        msg_email_blank = driver.find_element(
            By.XPATH, elem.msg_email_blank).text
        self.assertEqual(data.msg_email_blank, msg_email_blank)

    def test_failed_register_invalid_format_email(self):
        driver = self.driver
        register.register(driver, data.firstName, data.lastName,
                          data.emailInvalid, data.password, data.ConfirmPassword)
        msg_email_invalid = driver.find_element(
            By.XPATH, elem.msg_email_invalid).text
        self.assertEqual(data.msg_email_invalid, msg_email_invalid)

    def test_failed_register_password_blank(self):
        driver = self.driver
        register.register(driver, data.firstName, data.lastName,
                          data.email, data.passwordBlank, data.ConfirmPassword)
        msg_password_blank = driver.find_element(
            By.CSS_SELECTOR, elem.msg_password_blank).text
        self.assertEqual(data.msg_password_blank, msg_password_blank)
        msg_password_not_match = driver.find_element(
            By.CSS_SELECTOR, elem.msg_password_not_match).text
        self.assertEqual(data.msg_password_not_match, msg_password_not_match)

    def test_failed_register_confirm_password_blank(self):
        driver = self.driver
        register.register(driver, data.firstName, data.lastName,
                          data.email, data.password, data.ConfirmPasswordBlank)
        msg_confirm_password_blank = driver.find_element(
            By.CSS_SELECTOR, elem.msg_confirm_password_blank).text
        self.assertEqual(data.msg_password_blank, msg_confirm_password_blank)

    def test_failed_register_password_not_match(self):
        driver = self.driver
        register.register(driver, data.firstName, data.lastName,
                          data.email, data.password, data.ConfirmPasswordInvalid)
        msg_password_not_match = driver.find_element(
            By.CSS_SELECTOR, elem.msg_password_not_match).text
        self.assertEqual(data.msg_password_not_match, msg_password_not_match)

    def test_failed_register_password_less_6_char(self):
        driver = self.driver
        register.register(driver, data.firstName, data.lastName,
                          data.email, data.passwrod_less_6, data.ConfirmPassword)
        msg_password_less_6_char = driver.find_element(
            By.CSS_SELECTOR, elem.msg_password_blank).text
        self.assertEqual(data.msg_password_less_6_char,
                         msg_password_less_6_char)
        msg_password_not_match = driver.find_element(
            By.CSS_SELECTOR, elem.msg_password_not_match).text
        self.assertEqual(data.msg_password_not_match, msg_password_not_match)

    def test_failed_register_email_already_registered(self):
        driver = self.driver
        register.register(driver, data.firstName, data.lastName,
                          data.email, data.password, data.ConfirmPassword)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
