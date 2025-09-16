from compontents.authentication.registration_form_component import RegistrationFormComponent
from pages.base_page import BasePage
from playwright.sync_api import Page
from elements.button import Button

class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.form = RegistrationFormComponent(page)
        self.registration_button = Button(page, 'registration-page-registration-button', 'Registration')

    def click_registration_button(self):
        self.registration_button.click()