from selenium.webdriver.common.by import By

PAR_CARD_LINK = lambda number_par: (By.CSS_SELECTOR, f"ul.par-options li[data-value='{number_par}'] button")
PAR_CURRENT_INPUT = (By.CSS_SELECTOR, "input[name=nominal_value]")
