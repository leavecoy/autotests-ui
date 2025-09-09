from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Идем на сайт
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    # Находим и заполняем поле Email
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    # Находим и заполняем поле Username
    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    # Находим и заполняем поле Password
    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    # Нажимаем кнопку регистрации
    reg_btn = page.get_by_test_id('registration-page-registration-button')
    reg_btn.click()

    # Убеждаемся что видим Dashboard
    dashboard = page.get_by_test_id('dashboard-drawer-list-item-title-text')
    expect(dashboard).to_be_visible()


