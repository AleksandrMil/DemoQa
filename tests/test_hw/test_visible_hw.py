from pages.demoqa import Demoqa
from pages.accordian import Accordian



def test_visible_accordion(browser):
    demo_qa_page = Demoqa(browser)
    elements_page = Accordian(browser)
    demo_qa_page.visit()

