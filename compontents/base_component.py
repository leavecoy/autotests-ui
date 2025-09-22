from playwright.sync_api import Page, expect
from typing import Pattern
from tools.logger import get_logger
import allure

logger = get_logger("BASE_COMPONENT")

class BaseComponent:
    def __init__(self, page: Page):
        self.page = page

    def check_current_url(self, expected_url: Pattern[str]):
        step = f'Checking that current url equal expected url "{expected_url}"'
        with allure.step(step):
            logger.info(step)
            expect(self.page).to_have_url(expected_url)
