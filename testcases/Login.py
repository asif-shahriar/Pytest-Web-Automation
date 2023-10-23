import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import locator_factory.login_selectors as login_selectors


class Login:
    def __init__(self, email, passwd):
        self.login_email = email
        self.login_password = passwd

    def login(self, driver):
        wait = WebDriverWait(driver, 15)
        btnLogin = wait.until(ec.element_to_be_clickable((By.LINK_TEXT, login_selectors.btnLogin)))
        btnLogin.click()
        email = wait.until(ec.element_to_be_clickable((By.NAME, login_selectors.email)))
        email.send_keys(self.login_email)
        driver.find_element(By.ID, login_selectors.password).send_keys(self.login_password)
        submit = driver.find_elements(By.CSS_SELECTOR, login_selectors.submit)
        submit[1].click()
        time.sleep(1)
        logOutBtn = driver.find_element(By.LINK_TEXT, login_selectors.logOutBtn).is_displayed()
        if logOutBtn:
            print("Log in successful")
        else:
            print("Log out button is not displayed")

    def login_with_wrong_password(self, driver):
        wait = WebDriverWait(driver, 15)
        btnLogin = wait.until(ec.element_to_be_clickable((By.LINK_TEXT, login_selectors.btnLogin)))
        btnLogin.click()
        email = wait.until(ec.element_to_be_clickable((By.NAME, login_selectors.email)))
        email.send_keys(self.login_email)
        driver.find_element(By.ID, login_selectors.password).send_keys(self.login_password)
        submit = driver.find_elements(By.CSS_SELECTOR, login_selectors.submit)
        submit[1].click()
        time.sleep(1)

        assert 'Login was unsuccessful' in driver.page_source
