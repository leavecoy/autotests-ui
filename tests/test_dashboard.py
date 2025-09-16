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
    dashboard_page_with_state.dashboard_toolbar_view.check_visible()

    # Проверяем график Students
    dashboard_page_with_state.students_chart.check_visible(title='Students')

    # Проверяем график Activities
    dashboard_page_with_state.activities_chart.check_visible(title='Activities')

    # Проверяем график Courses
    dashboard_page_with_state.courses_chart.check_visible(title='Courses')

    # Проверяем график Scores
    dashboard_page_with_state.scores_chart.check_visible(title='Scores')
