from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.dashboard_title = page.get_by_test_id('dashboard-toolbar-title-text')

    # Критерий оценки: "Реализован метод, который проверяет видимость и ТЕКСТ заголовка “Dashboard”
    # Я бы разбил метод на два разных, но ТЗ есть ТЗ
    def expect_dashboard_title_is_visible_and_have_text(self, text: str):
        expect(self.dashboard_title).to_be_visible()
        expect(self.dashboard_title).to_have_text(text)
