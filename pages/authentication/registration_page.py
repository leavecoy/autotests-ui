import re

from compontents.authentication.registration_form_component import RegistrationFormComponent
from pages.base_page import BasePage
from playwright.sync_api import Page
from elements.button import Button
from elements.link import Link

class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.form = RegistrationFormComponent(page)
        self.login_link = Link(page, 'registration-page-login-link', 'Link')
        self.registration_button = Button(page, 'registration-page-registration-button', 'Registration')

    def click_login_link(self):
        self.login_link.click()
        self.check_current_url(re.compile(".*/#/auth/login"))

    def click_registration_button(self):
        self.registration_button.click()