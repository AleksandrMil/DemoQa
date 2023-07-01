from pages.base_page import BasePage
from components.components import WebElement

import time
class ElementsPage(BasePage):

    def __init__(self, driver):

        self.base_url = "https://demoqa.com/elements"
        super().__init__(driver, self.base_url)

        self.text_el = WebElement(driver, '.playgound-header > div')
        self.btn_1 = WebElement(driver, 'div:nth-child(1) > span > div')
        self.btn_1_textbox = WebElement(driver, '#app > div > div > div.row > div:nth-child(1) > div > div > div:nth-child(1) > div > ul>#item-0')
        self.btn_1_checkbox = WebElement(driver, 'div:nth-child(1) > div > ul>#item-1')
        self.icon = WebElement(driver, '#app > header > a')
        self.btns_first_menu = WebElement(driver, "div:nth-child(1)>div>ul>li")






    # def equal_url(self):
    #     if self.get_url() == self.base_url:
    #         return True
    #     return False
