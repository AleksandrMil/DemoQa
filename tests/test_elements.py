from pages.demoqa import Demoqa
from pages.elements_page import ElementsPage


def test_find_elements(browser):
    demo_qa_page = Demoqa(browser)
    elements_page = ElementsPage(browser)
    elements_page.visit()
    assert elements_page.btns_first_menu.check_count_elements(count=9)
