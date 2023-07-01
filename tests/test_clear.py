from pages.demoqa import Demoqa
from pages.text_box import TextBoxPage
import time

def test_clear(browser):
    text_box_page = TextBoxPage(browser)
    text_box_page.visit()

    text_box_page.fn.send_keys('goga')
    time.sleep(3)
    text_box_page.fn.clear()
    time.sleep(3)
    assert text_box_page.fn.get_text() == ''

