from selenium.webdriver.common.by import By
from PageObject.locator import elem
from PageObject.data import data


def testLogin(driver, inputEmail, inputPassword):
    driver.get(data.baseURL+"login")
    driver.maximize_window()
    driver.find_element(By.ID, elem.Email).send_keys(inputEmail)
    driver.find_element(By.ID, elem.Password).send_keys(inputPassword)
    driver.find_element(By.CLASS_NAME, elem.login_btn).click()
