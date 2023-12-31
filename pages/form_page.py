from pages.base_page import BasePage
from components.components import WebElement

import time
class FormPage(BasePage):
    def __init__(self, driver):
        self.base_url = "https://demoqa.com/automation-practice-form"
        super().__init__(driver, self.base_url)

        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.user_email = WebElement(driver, '#userEmail')
        self.gender_radio_1 = WebElement(driver, '#gender-radio-1')
        self.user_namber = WebElement(driver, '#userNumber')
        self.btn_submit = WebElement(driver, '#submit')
        self.modal_dialog = WebElement(driver, '#body>div.dade.modal.show>div')
        self.btn_close_modal = WebElement(driver, '#closeLargeModal')
        self.hobbies = WebElement(driver, '#hobbies-checkbox-1')
        self.curent_address = WebElement(driver, '#currentAddress')

        self.SC = WebElement(driver, '#state > div > div.css-1wy0on6 > div')













