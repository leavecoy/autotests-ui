import pytest
from pages.dashboard_page import DashboardPage

@pytest.mark.dashboard
@pytest.mark.regression
def test_dashboard_displaying(dashboard_page_with_state: DashboardPage):

    # Переходим на страницу
    dashboard_page_with_state.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')

    # Проверяем навбар
    dashboard_page_with_state.navbar.check_visible('username')

    # Проверяем сайдбар
    dashboard_page_with_state.sidebar.check_visible()

    # Проверяем заголовок
    dashboard_page_with_state.check_visible_dashboard_title()

    # Проверяем график Students
    dashboard_page_with_state.check_visible_students_chart()

    # Проверяем график Activities
    dashboard_page_with_state.check_visible_activities_chart()

    # Проверяем график Courses
    dashboard_page_with_state.check_visible_courses_chart()

    # Проверяем график Scores
    dashboard_page_with_state.check_visible_scores_chart()
