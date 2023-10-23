import pytest

from testcases.Login import Login
import Test_Run1 as registration
import environment.configure as setupEnvironment
from utilities import JsonFactories

driver = None
registration_directory = "Enter your registration.json directory(absolute) here with double forward slash"


@pytest.fixture(scope="function", autouse=True, name="Initializing driver & teardown methods")
def test_setup():
    global driver
    setup = setupEnvironment.Setup()
    driver = setup.setup("Edge")
    yield
    print("Closing the browser")
    driver.close()


@pytest.mark.run(order=1)
@pytest.mark.smoke
def test_login():
    global driver
    if registration.LOGIN_EMAIL is None:
        '''
        If the global variables returns None, the method will take 
        a previously created user credentials.
        '''
        login = Login("estevens@example.org", ")%f77H6Kmu")
    else:
        login = Login(registration.LOGIN_EMAIL, registration.LOGIN_PASSWORD)

    driver.get("https://demo.nopcommerce.com")
    login.login(driver)


@pytest.mark.run(order=2)
@pytest.mark.regression
def test_loginWithInvalidPassword():
    global driver
    login = Login(registration.LOGIN_EMAIL, "wrong password")
    driver.get("https://demo.nopcommerce.com")
    login.login_with_wrong_password(driver)


@pytest.mark.run(order=3)
@pytest.mark.skip(reason="I am skipping this")
@pytest.mark.regression
def test_login_from_json():
    global driver, registration_directory
    if JsonFactories.readJson(registration_directory, "email_address") is "":
        '''
        If the json email key returns empty string, the method will take 
        a previously created user credentials.
        '''
        login = Login("estevens@example.org", ")%f77H6Kmu")
    else:
        login = Login(JsonFactories.readJson(registration_directory, "email_address"),
                      JsonFactories.readJson(registration_directory, "passwrd"))
    driver.get("https://demo.nopcommerce.com")
    login.login(driver)
