import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from PageObject.locator import elem
from PageObject.data import data, title
import login
import time


class Checkout(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_checkout_success(self):
        driver = self.driver
        login.testLogin(driver, data.email, data.password)
        driver.find_element(By.XPATH, elem.add_to_cart).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, elem.recipient_name)))
        url = driver.current_url
        self.assertEqual(
            url, "https://demowebshop.tricentis.com/25-virtual-gift-card")
        driver.find_element(By.ID, elem.recipient_name).send_keys(
            "Aldian Karim")
        driver.find_element(
            By.ID, elem.recipient_email).send_keys("Aldian@gmail.com")
        sender_name = driver.find_element(
            By.ID, elem.sender_name)
        sender_name.clear()
        sender_name.send_keys("Aldian Karim")
        sender_email = driver.find_element(
            By.ID, elem.sender_email)
        sender_email.clear()
        sender_email.send_keys("Aldian@gmail.com")
        driver.find_element(By.ID, elem.form_message).send_keys(
            "Testing produk")
        qty = driver.find_element(By.ID, elem.form_qty)
        qty.clear()
        qty.send_keys(1)
        WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.ID, elem.btn_add_to_cart_2)))
        driver.find_element(By.ID, elem.btn_add_to_cart_2).click()
        WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".content")))
        allert_success = driver.find_element(
            By.CSS_SELECTOR, elem.content).text
        self.assertEqual(allert_success, title.allert_success)
        driver.find_element(
            By.XPATH, "//*[@id='topcartlink']/a/span[1]").click()
        page_title = driver.find_element(By.CSS_SELECTOR, elem.page_title).text
        self.assertEqual(page_title, "Shopping cart")
        driver.find_element(By.ID, elem.terms_of_service).click()
        WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.ID, elem.btn_checkout)))
        driver.find_element(By.ID, elem.btn_checkout).click()

        # PAGE CHEKCOUT
        WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, elem.page_title)))
        page_title_1 = driver.find_element(
            By.CSS_SELECTOR, elem.page_title).text
        self.assertEqual(page_title_1, "Checkout")
        url_checkout = driver.current_url
        self.assertEqual(
            url_checkout, "https://demowebshop.tricentis.com/onepagecheckout")

        # Sudah terdaftar

        driver.find_element(
            By.ID, "BillingNewAddress_Company").send_keys("Company Test")
        sel = Select(driver.find_element(By.ID, elem.dropdown_country))
        sel.select_by_value("86")
        driver.find_element(
            By.ID, elem.form_city).send_keys("Jakarta")
        driver.find_element(
            By.ID, elem.form_address_1).send_keys("Jalan Durian")
        driver.find_element(
            By.ID, elem.form_postal_code).send_keys(12620)
        driver.find_element(
            By.ID, elem.form_phone_number).send_keys("087786370441")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, elem.btn_continue)))
        driver.find_element(By.XPATH, elem.btn_continue).click()

        # Select Payment Method
        # WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.ID, elem.title_pay_method)))
        title_pay_method = driver.find_element(
            By.ID, elem.title_pay_method).text
        self.assertEqual(title_pay_method, title.title_pay_method)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, elem.btn_continue_2)))
        driver.find_element(By.XPATH, elem.btn_continue_2).click()

        # Payment Information
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//*[@id='opc-payment_info']")))
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, elem.btn_continue_3)))
        driver.find_element(By.XPATH, elem.btn_continue_3).click()

        # Confirm Order
        WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.ID, elem.title_confirm_order)))
        title_confirm_order = driver.find_element(
            By.ID, elem.title_confirm_order).text
        self.assertEqual(title_confirm_order, title.title_confirm_order)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, elem.btn_continue_4)))
        driver.find_element(By.XPATH, elem.btn_continue_4).click()

        # Order Success
        WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.XPATH, elem.msg_success_order)))
        url_success_checkout = driver.current_url
        self.assertEqual(url_success_checkout,
                         "https://demowebshop.tricentis.com/checkout/completed/")
        msg_success_order = driver.find_element(
            By.XPATH, elem.msg_success_order).text
        self.assertEqual(msg_success_order, data.msg_success_order)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, elem.btn_continue_5)))
        driver.find_element(By.XPATH, elem.btn_continue_5).click()
        url_success_checkout = driver.current_url
        self.assertEqual(url_success_checkout,
                         "https://demowebshop.tricentis.com/")

    def test_failed_recipient_name_blank(self):
        driver = self.driver
        login.testLogin(driver, data.email, data.password)
        driver.find_element(By.XPATH, elem.add_to_cart).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, elem.recipient_name)))
        url = driver.current_url
        self.assertEqual(
            url, "https://demowebshop.tricentis.com/25-virtual-gift-card")
        driver.find_element(By.ID, elem.recipient_name).send_keys(
            "")
        driver.find_element(
            By.ID, elem.recipient_email).send_keys("Aldian@gmail.com")
        sender_name = driver.find_element(
            By.ID, elem.sender_name)
        sender_name.clear()
        sender_name.send_keys("Aldian Karim")
        sender_email = driver.find_element(
            By.ID, elem.sender_email)
        sender_email.clear()
        sender_email.send_keys("Aldian@gmail.com")
        driver.find_element(By.ID, elem.form_message).send_keys(
            "Testing produk")
        qty = driver.find_element(By.ID, elem.form_qty)
        qty.clear()
        qty.send_keys(1)
        WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.ID, elem.btn_add_to_cart_2)))
        driver.find_element(By.ID, elem.btn_add_to_cart_2).click()

        # Validation Alert
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, elem.msg_content_checkout)))
        msg_invalid_recipient_name = driver.find_element(
            By.XPATH, elem.msg_content_checkout).text
        self.assertEqual(msg_invalid_recipient_name,
                         data.msg_invalid_recipient_name)

    def test_failed_recipient_email_blank(self):
        driver = self.driver
        login.testLogin(driver, data.email, data.password)
        driver.find_element(By.XPATH, elem.add_to_cart).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, elem.recipient_name)))
        url = driver.current_url
        self.assertEqual(
            url, "https://demowebshop.tricentis.com/25-virtual-gift-card")
        driver.find_element(By.ID, elem.recipient_name).send_keys(
            "Aldian Karim")
        driver.find_element(
            By.ID, elem.recipient_email).send_keys("")
        sender_name = driver.find_element(
            By.ID, elem.sender_name)
        sender_name.clear()
        sender_name.send_keys("Aldian Karim")
        sender_email = driver.find_element(
            By.ID, elem.sender_email)
        sender_email.clear()
        sender_email.send_keys("Aldian@gmail.com")
        driver.find_element(By.ID, elem.form_message).send_keys(
            "Testing produk")
        qty = driver.find_element(By.ID, elem.form_qty)
        qty.clear()
        qty.send_keys(1)
        WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.ID, elem.btn_add_to_cart_2)))
        driver.find_element(By.ID, elem.btn_add_to_cart_2).click()

        # Validation Alert
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, elem.msg_content_checkout)))
        msg_invalid_recipient_email = driver.find_element(
            By.XPATH, elem.msg_content_checkout).text
        self.assertEqual(msg_invalid_recipient_email,
                         data.msg_invalid_recipient_email)

    def test_failed_sender_name_blank(self):
        driver = self.driver
        login.testLogin(driver, data.email, data.password)
        driver.find_element(By.XPATH, elem.add_to_cart).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, elem.recipient_name)))
        url = driver.current_url
        self.assertEqual(
            url, "https://demowebshop.tricentis.com/25-virtual-gift-card")
        driver.find_element(By.ID, elem.recipient_name).send_keys(
            "Aldian Karim")
        driver.find_element(
            By.ID, elem.recipient_email).send_keys("gepengkrn13026@gmail.com")
        sender_name = driver.find_element(
            By.ID, elem.sender_name)
        sender_name.clear()
        sender_name.send_keys("")
        sender_email = driver.find_element(
            By.ID, elem.sender_email)
        sender_email.clear()
        sender_email.send_keys("Aldian@gmail.com")
        driver.find_element(By.ID, elem.form_message).send_keys(
            "Testing produk")
        qty = driver.find_element(By.ID, elem.form_qty)
        qty.clear()
        qty.send_keys(1)
        WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.ID, elem.btn_add_to_cart_2)))
        driver.find_element(By.ID, elem.btn_add_to_cart_2).click()

        # Validation Alert
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, elem.msg_content_checkout)))
        msg_invalid_sender_name = driver.find_element(
            By.XPATH, elem.msg_content_checkout).text
        self.assertEqual(msg_invalid_sender_name,
                         data.msg_invalid_sender_name)

    def test_failed_sender_email_blank(self):
        driver = self.driver
        login.testLogin(driver, data.email, data.password)
        driver.find_element(By.XPATH, elem.add_to_cart).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, elem.recipient_name)))
        url = driver.current_url
        self.assertEqual(
            url, "https://demowebshop.tricentis.com/25-virtual-gift-card")
        driver.find_element(By.ID, elem.recipient_name).send_keys(
            "Aldian Karim")
        driver.find_element(
            By.ID, elem.recipient_email).send_keys("gepengkrn13026@gmail.com")
        sender_name = driver.find_element(
            By.ID, elem.sender_name)
        sender_name.clear()
        sender_name.send_keys("Aldian Karim")
        sender_email = driver.find_element(
            By.ID, elem.sender_email)
        sender_email.clear()
        sender_email.send_keys("")
        driver.find_element(By.ID, elem.form_message).send_keys(
            "Testing produk")
        qty = driver.find_element(By.ID, elem.form_qty)
        qty.clear()
        qty.send_keys(1)
        WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.ID, elem.btn_add_to_cart_2)))
        driver.find_element(By.ID, elem.btn_add_to_cart_2).click()

        # Validation Alert
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, elem.msg_content_checkout)))
        msg_invalid_email_name = driver.find_element(
            By.XPATH, elem.msg_content_checkout).text
        self.assertEqual(msg_invalid_email_name,
                         data.msg_invalid_email_name)

    def test_failed_qty_blank(self):
        driver = self.driver
        login.testLogin(driver, data.email, data.password)
        driver.find_element(By.XPATH, elem.add_to_cart).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, elem.recipient_name)))
        url = driver.current_url
        self.assertEqual(
            url, "https://demowebshop.tricentis.com/25-virtual-gift-card")
        driver.find_element(By.ID, elem.recipient_name).send_keys(
            "Aldian Karim")
        driver.find_element(
            By.ID, elem.recipient_email).send_keys(data.email)
        sender_name = driver.find_element(
            By.ID, elem.sender_name)
        sender_name.clear()
        sender_name.send_keys("Aldian Karim")
        sender_email = driver.find_element(
            By.ID, elem.sender_email)
        sender_email.clear()
        sender_email.send_keys(data.email)
        driver.find_element(By.ID, elem.form_message).send_keys(
            "Testing produk")
        qty = driver.find_element(By.ID, elem.form_qty)
        qty.clear()
        qty.send_keys("")
        WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.ID, elem.btn_add_to_cart_2)))
        driver.find_element(By.ID, elem.btn_add_to_cart_2).click()

        # Validation Alert
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, elem.msg_content_checkout)))
        msg_invalid_qty = driver.find_element(
            By.XPATH, elem.msg_content_checkout).text
        self.assertEqual(msg_invalid_qty,
                         data.msg_invalid_qty)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
