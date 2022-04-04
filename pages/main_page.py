from .locators import MainPageLocators
from .base_page import BasePage
import requests


class MainPage(BasePage):
    def should_be_footer(self):
        assert self.is_element_present(*MainPageLocators.FOOTER_FORM), "footer is not available"

    def should_be_header(self):
        assert self.is_element_present(*MainPageLocators.HEADERS_FORM), "header is not available"

    def request_should_be_200(self, links):
        bad_url = []
        for link in links:
            if requests.get(link.get_attribute("href")).status_code != 200:
                bad_url.append(link.get_attribute("href"))
        assert len(bad_url) == 0, bad_url

