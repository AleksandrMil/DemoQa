import time

from pages.demoqa import Demoqa
from pages.elements_page import ElementsPage


def test_visible_btn_sidebar(browser):
    # demo_qa_page = Demoqa(browser)
    elements_page = ElementsPage(browser)
    # demo_qa_page.visit()
    elements_page.visit()
    #elements_page.btn_1.click()
    time.sleep(3)
    # assert elements_page.btn_1_textbox.exist()
    assert elements_page.btn_1_textbox.visible()


def test_not_visible_btn_sidebar(browser):
    elements_page = ElementsPage(browser)
    elements_page.visit()
    assert elements_page.btn_1_checkbox.visible()
    elements_page.btn_1.click()
    time.sleep(3)
    assert not elements_page.btn_1_checkbox.visible()




    # demo_qa_page.btn_elements.click()
