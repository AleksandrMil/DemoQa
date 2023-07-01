from pages.base_page import BasePage
from components.components import WebElement

import time
class Accordian(BasePage):

    def __init__(self, driver):

        self.base_url = "https://demoqa.com/accordian"
        super().__init__(driver, self.base_url)
