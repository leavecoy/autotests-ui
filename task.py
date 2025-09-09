from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    autorization_email_input = page.get_by_test_id('login-form-email-input').locator('input')
    expect(autorization_email_input).to_be_visible()

    autorization_password_input = page.get_by_test_id('login-form-password-input').locator('input')
    expect(autorization_password_input).to_be_visible()

    autorization_login_button = page.get_by_test_id('login-page-login-button')
    expect(autorization_login_button).to_be_visible()

    login_button = page.get_by_test_id('login-page-login-button')
    expect(login_button).to_be_visible()

    redirect_to_registration_button = page.get_by_test_id('login-page-registration-link')
    redirect_to_registration_button.click()

    registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    expect(registration_email_input).to_be_visible()

    registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    expect(registration_password_input).to_be_visible()

    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_visible()
