from playwright.sync_api import sync_playwright, expect, Page
import pytest

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):

    chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    # Проверяем элемент "Courses"
    courses_element = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_element).to_have_text('Courses')

    # Проверяем элемент "There is no results"
    no_results_element = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(no_results_element).to_have_text('There is no results')

    # Проверяем иконку
    list_empty_icon_element = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(list_empty_icon_element).to_be_visible()

    # Проверяем элемент "courses-list-empty-view-description-text"
    list_empty_desc = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(list_empty_desc).to_have_text('Results from the load test pipeline will be displayed here')