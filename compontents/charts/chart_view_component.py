from compontents.base_component import BaseComponent
from playwright.sync_api import Page
from elements.text import Text
from elements.image import Image
import allure

class ChartViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str, chart_type: str):
        super().__init__(page)

        self.title_text = Text(page, f'{identifier}-widget-title-text', 'Title')
        self.chart = Image(page, f'{identifier}-{chart_type}-chart', 'Chart')

    @allure.step('Check visible "{title}" chart view')
    def check_visible(self, title: str):
        self.title_text.check_visible()
        self.title_text.check_have_text(title)

        self.chart.check_visible()
