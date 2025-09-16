from compontents.base_component import BaseComponent
from playwright.sync_api import Page, expect


class CourseViewMenuComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu_button = self.page.get_by_test_id('course-view-menu-button')
        self.edit_menu_button = self.page.get_by_test_id('course-view-edit-menu-item')
        self.delete_menu_button = self.page.get_by_test_id('course-view-delete-menu-item')

    def click_edit(self, index: int):
        self.menu_button.nth(index).click()

        expect(self.edit_menu_button).to_be_visible()
        self.edit_menu_button.click()

    def click_delete(self, index: int):
        self.delete_menu_button.nth(index).click()

        expect(self.delete_menu_button).to_be_visible()
        self.delete_menu_button.click()
