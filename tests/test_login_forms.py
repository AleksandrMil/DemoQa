from pages.form_page import  FormPage
import time

def test_go_to_page_elements(browser):
    form_page = FormPage(browser)
    form_page.visit()

    assert not form_page.modal_dialog.exist()
    time.sleep(3)

    form_page.first_name.send_keys('tester')
    form_page.last_name.send_keys('yesterov')
    form_page.user_email.send_keys('test@tt.tt')
    form_page.gender_radio_1.click_force()
    form_page.user_namber.send_keys('877888888888')
    form_page.hobbies.send_keys('blabla')
    form_page.curent_address.send_keys('fg ablfgsdfgsdfgsdfgsdfgsdfg ablfgsdfgsdfgsdfgsdfgsdfg a')
    time.sleep(3)
    form_page.btn_submit.click_force()
    time.sleep(3)
    form_page.SC.click_force()








