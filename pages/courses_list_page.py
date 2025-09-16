from compontents.views.empty_view_component import EmptyViewComponent
from pages.base_page import BasePage
from playwright.sync_api import Page, expect
from compontents.navigation.navbar_component import NavbarComponent
from compontents.navigation.sidebar_component import SidebarComponent
from compontents.courses.course_view_component import CourseViewComponent
from compontents.courses.courses_list_toolbar_view_component import CoursesListToolbarViewComponent

class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.empty_view = EmptyViewComponent(page, identifier='courses-list')
        self.course_view = CourseViewComponent(page)
        self.toolbar_view = CoursesListToolbarViewComponent(page)

    def check_visible_empty_view(self):
        self.empty_view.check_visible(
            title='There is no results',
            description='Results from the load test pipeline will be displayed here'
        )



