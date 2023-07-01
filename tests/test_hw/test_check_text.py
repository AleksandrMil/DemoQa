from pages.demoqa import Demoqa
from pages.elements_page import ElementsPage


def test_go_to_page_elements(browser):
    demo_qa_page = Demoqa(browser)
    elements_page = ElementsPage(browser)
    demo_qa_page.visit()
    demo_qa_page.btn_elements.click()

    elements_page.visit()
    assert elements_page.text_el.get_text() == 'Elements'

    assert elements_page.icon.exist()





    # assert demo_qa_page.equal_url()

    # assert elements_page.equal_url()