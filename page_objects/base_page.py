from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from locators import CommonLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def clic_to_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def wait_overlay(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.invisibility_of_element(CommonLocators.OVERLAY2))
        WebDriverWait(self.driver, 5).until(expected_conditions.invisibility_of_element(CommonLocators.OVERLAY1))

    def click_to_element_with_wait_overlay(self, locator):
        self.wait_overlay()
        self.clic_to_element(locator)

    def drag_and_drop_element(self, element, target):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(element))
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(target))
        action = ActionChains(self.driver)
        action.drag_and_drop(self.driver.find_element(*element), self.driver.find_element(*target)).perform()

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text
