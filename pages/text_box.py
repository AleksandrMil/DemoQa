from pages.base_page import BasePage
from components.components import WebElement

import time
class TextBoxPage(BasePage):

    def __init__(self, driver):

        self.base_url = "https://demoqa.com/text-box"
        super().__init__(driver, self.base_url)

        self.fn = WebElement(driver, '#userName')
