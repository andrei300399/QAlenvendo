import allure
from ui_test.pages.MainPage import MainPage
from ui_test import locators
import pytest


class TestCase:
    @pytest.mark.UI
    def test_denomination(self, driver):
        par_numbers = ['500', '1000', '2000', '3000', '5000', '10000']
        main_page = MainPage(driver)
        for par in par_numbers:
            with allure.step(f"Select par card {par}"):
                main_page.select_par(par)
                card = main_page.find(locators.PAR_CARD_LINK(par))
            with allure.step(f"Check active par card {par}"):
                assert 'button--active' in card.get_attribute('class')
            with allure.step(f"Check input par card {par}"):
                assert par in main_page.get_current_input_value_par()
