from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

NAME = "Swapan"


class BaseDriver(object):

    def __init__(self, browser):
        self.browser = browser
        if self.browser.lower() == "chrome":
            self.driver = webdriver.Chrome(executable_path=r"C:\BrowserDriver\chromedriver.exe")
        elif self.browser.lower() == "firefox":
            self.driver = webdriver.Firefox(executable_path=r"")
        elif self.browser.lower() == "ie":
            self.driver = webdriver.Ie(executable_path=r"")
        else:
            self.driver = webdriver.Chrome(executable_path=r"C:\BrowserDriver\chromedriver.exe")

        self.waitDriver = WebDriverWait(self.driver, 10, 1, ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])

    @staticmethod
    def get_by_type(locator_type='id'):
        if locator_type.lower() == 'id':
            return By.ID
        if locator_type.lower() == "xpath":
            print(NAME + "testing global variable")
            return By.XPATH
        if locator_type.lower() == "css":
            return By.CSS_SELECTOR

    def get_element(self, locator="", locator_type="id"):
        by_type = BaseDriver.get_by_type(locator_type)
        element = self.driver.find_element(by_type, locator)
        return element

    def click_element(self, locator="", locator_type="id"):
        element = self.get_element(locator=locator, locator_type=locator_type)
        try:
            element.click()
        except ElementClickInterceptedException:
            print("element was not click able")

    def validate_element_present(self,locator="", locator_type="id"):
        try:
            element = self.get_element(locator=locator, locator_type=locator_type)
            if element.is_displayed():
                return True
            else:
                return False
        except ElementNotVisibleException:
            return False

    def send_kyes_to_element(self, locator="", locator_type="id", input_text=""):
        element = self.get_element(locator, locator_type)
        element.send_keys(input_text)

    def wait_n_get_element(self, locator="", locator_type="id"):
        by_type = self.get_by_type(locator_type)
        wait_element = self.waitDriver.until(EC.element_to_be_clickable((by_type, locator)))
        return wait_element

    def wait_n_click_element(self, locator="", locator_type="id"):
        wait_element = self.wait_n_get_element(locator, locator_type)
        wait_element.click()

    def wait_n_send_keys(self, locator="", locator_type="id", input_text=""):
        element = self.wait_n_get_element(locator, locator_type)
        element.send_keys(input_text)

    def move_to_frame(self, locator, locator_type):
        self.driver.switch_to.frame(self.get_element(locator, locator_type))




