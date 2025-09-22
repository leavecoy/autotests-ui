from typing import Any, Generator
import pytest
from playwright.sync_api import Page, Playwright
from pages.authentication.registration_page import RegistrationPage
from _pytest.fixtures import SubRequest
from tools.playwright.pages import initialize_playwright_page
from config import settings
from tools.routes import AppRoute

# PyCharm ругается что функция ничего не возвращает (бесит), добавил Generator
@pytest.fixture(params=settings.browsers)
def page(request: SubRequest, playwright: Playwright) -> Generator[Page, Any, None]:
    yield from initialize_playwright_page(
        playwright,
        test_name=request.node.name,
        browser_type=request.param
    )

@pytest.fixture(scope="session")
def initialize_browser_state(playwright : Playwright):
    browser = playwright.chromium.launch(headless=settings.headless)
    context = browser.new_context(base_url=settings.get_base_url())
    page = context.new_page()

    registration_page = RegistrationPage(page=page)
    registration_page.visit(AppRoute.REGISTRATION)
    registration_page.form.fill(
        email=settings.test_user.email,
        username=settings.test_user.username,
        password=settings.test_user.password
    )
    registration_page.click_registration_button()

    # Сохраняем состояние браузера
    context.storage_state(path=settings.browser_state_file)
    browser.close()

# PyCharm ругается что функция ничего не возвращает (бесит), добавил Generator
@pytest.fixture(params=settings.browsers, scope="function")
def page_with_state(
        request: SubRequest, initialize_browser_state, playwright : Playwright
) -> Generator[Page, Any, None]:
    yield from initialize_playwright_page(
        playwright,
        test_name=request.node.name,
        storage_state=settings.browser_state_file,
        browser_type=request.param
    )

