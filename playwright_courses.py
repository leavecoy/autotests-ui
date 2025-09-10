from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

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

    # Сохраняем состояние браузера
    context.storage_state(path='browser-state.json')

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    # Проверяем элемент "Courses"
    courses_element = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_element).to_have_text('Courses')

    # Проверяем элемент "There is no results"
    no_results_element = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(no_results_element).to_have_text('There is no results')

    # Проверяем иконку
    list_empty_icon_element = page.get_by_test_id('courses-list-empty-view-icon')
    expect(list_empty_icon_element).to_be_visible()

    # Проверяем элемент "courses-list-empty-view-description-text"
    list_empty_desc = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(list_empty_desc).to_have_text('Results from the load test pipeline will be displayed here')

