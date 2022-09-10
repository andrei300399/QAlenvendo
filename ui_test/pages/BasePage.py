from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.driver.implicitly_wait(timeout)

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 15
        return WebDriverWait(self.driver, timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.visibility_of_element_located(locator))

    def click(self, locator, timeout=None):
        self.find(locator, timeout)
        self.wait(timeout).until(EC.element_to_be_clickable(locator)).click()
