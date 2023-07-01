from pages.demoqa import Demoqa
from pages.elements_page import ElementsPage


def test_seo(browser):
    demo_qa_page = Demoqa(browser)

    demo_qa_page.visit()
    assert browser.title == "DEMOQA"


