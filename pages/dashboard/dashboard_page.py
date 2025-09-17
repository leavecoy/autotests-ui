from compontents.charts.chart_view_component import ChartViewComponent
from compontents.dashboard.dashboard_toolbar_view_component import DashboardToolbarViewComponent
from compontents.navigation.navbar_component import NavbarComponent
from compontents.navigation.sidebar_component import SidebarComponent
from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.dashboard_toolbar_view = DashboardToolbarViewComponent(page)
        self.students_chart = ChartViewComponent(page, identifier='students', chart_type='bar')
        self.activities_chart = ChartViewComponent(page, identifier='activities', chart_type='line')
        self.courses_chart = ChartViewComponent(page, identifier='courses', chart_type='pie')
        self.scores_chart = ChartViewComponent(page, identifier='scores', chart_type='scatter')

