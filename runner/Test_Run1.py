from testcases.Registration import Registration
import environment.configure as setupEnvironment
import pytest

LOGIN_EMAIL = None
LOGIN_PASSWORD = None


@pytest.fixture(scope="function", autouse=True, name="Initializing driver & teardown methods")
def test_setup():
    global driver
    setup = setupEnvironment.Setup()
    driver = setup.setup("Edge")
    yield driver
    print("Closing the browser")
    driver.close()


@pytest.mark.run(order=1)
@pytest.mark.smoke
@pytest.mark.regression
def test_registration():
    global LOGIN_EMAIL, LOGIN_PASSWORD
    driver.get("https://demo.nopcommerce.com")
    registration = Registration()
    registration.registration(driver)
    LOGIN_EMAIL = registration.login_email
    LOGIN_PASSWORD = registration.login_password

