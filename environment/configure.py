from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options


class Setup:

    def __init__(self):
        self.driver = webdriver

    def setup(self, browser: str):

        driver = None
        browser_name = browser.lower()

        if 'chrome' in browser_name:
            ops = Options()
            ops.add_argument("--headless=new")
            ops.add_argument('window-size=1920x1080')
            ops.add_experimental_option("detach", True)
            driver = self.driver.Chrome(service=Service(ChromeDriverManager().install(), options=ops))

        elif 'edge' in browser_name:
            edge_ops = EdgeOptions()
            edge_ops.add_argument("headed")
            edge_ops.add_argument('window-size=1920x1080')
            edge_ops.add_experimental_option("detach", True)
            driver = self.driver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=edge_ops)

        driver.implicitly_wait(15)
        driver.set_page_load_timeout(60)
        driver.maximize_window()
        print("Driver launched successfully!!")
        return driver

