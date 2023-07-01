from pages.demoqa import Demoqa
from pages.text_box import TextBoxPage
import time

def test_clear(browser):
    text_box_page = TextBoxPage(browser)
    text_box_page.visit()

    assert text_box_page.fn.get_dom_attribute('placeholder') == 'Full Name'