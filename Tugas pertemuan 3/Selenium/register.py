from selenium.webdriver.common.by import By
from PageObject.locator import elem
from PageObject.data import data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def register(driver, inputFirstName, inputLastname, inputEmail, inputPassword, inputConfirmPassword):
    driver.get(data.baseURL+"register")
    driver.maximize_window()
    driver.find_element(By.ID, elem.gender).click()
    driver.find_element(By.ID, elem.FirstName).send_keys(inputFirstName)
    driver.find_element(By.ID, elem.LastName).send_keys(inputLastname)
    driver.find_element(By.ID, elem.Email).send_keys(inputEmail)
    driver.find_element(By.ID, elem.Password).send_keys(inputPassword)
    driver.find_element(By.ID, elem.ConfirmPassword).send_keys(
        inputConfirmPassword)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, elem.register_btn)))
    driver.find_element(By.ID, elem.register_btn).click()
