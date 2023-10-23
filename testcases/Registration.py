from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from faker import Faker
from utilities import JsonFactories
import locator_factory.registration_selectors as registration_selector


class Registration:
    login_email = None
    login_password = None
    registration_json_directory = "Enter your registration.json directory(absolute) here with double forward slash"

    def __init__(self):
        self.fake = Faker()

    def registration(self, driver):
        wait = WebDriverWait(driver, 15)
        actions = ActionChains(driver)
        assert "nopCommerce demo store" == driver.title

        btnRegister = wait.until(ec.element_to_be_clickable((By.LINK_TEXT, registration_selector.btnRegister)))
        btnRegister.click()
        btnGender = wait.until(ec.element_to_be_clickable((By.ID, registration_selector.btnGender)))
        btnGender.click()
        driver.find_element(By.ID, registration_selector.first_name).send_keys(self.fake.first_name())
        driver.find_element(By.ID, registration_selector.last_name).send_keys(self.fake.last_name())

        selectDay = Select(driver.find_element(By.NAME, registration_selector.selectDay))
        selectDay.select_by_visible_text("2")
        selectMonth = Select(driver.find_element(By.NAME, registration_selector.selectMonth))
        selectMonth.select_by_index(9)
        selectYear = Select(driver.find_element(By.NAME, registration_selector.selectYear))
        selectYear.select_by_value("1945")

        email = wait.until(ec.element_to_be_clickable((By.NAME, registration_selector.email)))
        Registration.login_email = self.fake.email()
        email.send_keys(Registration.login_email)

        newsLetter = driver.find_element(By.NAME, registration_selector.newsLetter)
        if newsLetter.is_selected():
            newsLetter.click()

        inputPass = driver.find_element(By.NAME, registration_selector.inputPass)
        confirmPass = driver.find_element(By.NAME, registration_selector.confirmPass)
        actions.scroll_to_element(inputPass)
        Registration.login_password = self.fake.password(10)

        inputPass.send_keys(Registration.login_password)
        confirmPass.send_keys(Registration.login_password)

        submit = wait.until(ec.element_to_be_clickable((By.XPATH, registration_selector.submit)))
        submit.click()

        assert 'Your registration completed' in driver.page_source
        JsonFactories.writeJson(Registration.registration_json_directory, "email_address", Registration.login_email)
        JsonFactories.writeJson(Registration.registration_json_directory, "passwrd", Registration.login_password)

