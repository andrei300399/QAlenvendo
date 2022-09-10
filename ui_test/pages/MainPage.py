from ui_test import locators
from .BasePage import BasePage



class MainPage(BasePage):

    def select_par(self, par_number):
        self.click(locators.PAR_CARD_LINK(par_number))

    def get_current_input_value_par(self):
        return self.find(locators.PAR_CURRENT_INPUT).get_attribute('value')
