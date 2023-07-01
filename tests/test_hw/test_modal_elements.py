from pages.demoqa import Demoqa
from pages.modal_dialogs_page import ModalDialogs


def test_modal_elements(browser):
    modal_dialogs_page = ModalDialogs(browser)
    modal_dialogs_page.visit()

    return len(submenu_buttons)
