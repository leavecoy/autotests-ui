from playwright.sync_api import sync_playwright, Page, expect
import pytest

@pytest.mark.regression
@pytest.mark.registration
def test_succesful_registration(chromium_page: Page):

    chromium_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    # Находим и заполняем поле Email
    email_input = chromium_page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    # Находим и заполняем поле Username
    username_input = chromium_page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    # Находим и заполняем поле Password
    password_input = chromium_page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    # Нажимаем кнопку регистрации
    reg_btn = chromium_page.get_by_test_id('registration-page-registration-button')
    reg_btn.click()

    # Проверяем элемент Dashboard
    dashboard_element = chromium_page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_element).to_have_text('Dashboard')
