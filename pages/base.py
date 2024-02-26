from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BaseFunction:
    def __init__(self, driver):
        self.driver = driver

    def click_by_locator(self, element_locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(element_locator)).click()

    def find_element_by_locator(self, element_locator):
        element = WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located(element_locator))
        return element
