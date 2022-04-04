from .pages.main_page import MainPage


def test_guest_should_see_footer(browser):
    link = "https://www.mos.ru/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_footer()


def test_guest_should_see_header(browser):
    link = "https://www.mos.ru/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_header()


def test_request_all_links(browser):
    link = "https://www.mos.ru/"
    page = MainPage(browser, link)
    page.open()
    page.request_should_be_200(browser.find_elements_by_tag_name("a"))




