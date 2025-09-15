from playwright.sync_api import expect, Page
import pytest
from pages.create_course_page import CreateCoursePage
from pages.courses_list_page import CoursesListPage

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(courses_list_page: CoursesListPage):
    courses_list_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    # Проверяем навбар
    courses_list_page.navbar.check_visible('username')

    # Проверяем сайдбар
    courses_list_page.sidebar.check_visible()

    # Проверяем наличие и корректное отображение заголовка страницы
    courses_list_page.check_visible_courses_title()

    # Проверяем, что кнопка для создания нового курса отображается
    courses_list_page.check_visible_create_course_button()

    # Проверяем, что при отсутствии курсов отображается соответствующий блок с сообщением об отсутствии результатов
    courses_list_page.check_visible_empty_view()

@pytest.mark.courses
@pytest.mark.regression
def test_create_course(create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
    create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')

    # Проверить наличие заголовка "Create course"
    create_course_page.check_visible_create_course_title()

    # Проверить, что кнопка создания курса недоступна для нажатия
    create_course_page.check_disabled_create_course_button()

    # Убедиться, что отображается пустой блок для предпросмотра изображения
    create_course_page.check_visible_image_preview_empty_view()

    # Проверить, что блок загрузки изображения отображается в состоянии, когда картинка не выбрана — метод
    create_course_page.check_visible_image_upload_view()

    # Проверить, что форма создания курса отображается и содержит значения по умолчанию
    create_course_page.check_visible_create_course_form(
        title='',
        estimated_time='',
        description='',
        max_score='0',
        min_score='0'
    )

    # Проверить наличие заголовка "Exercises"
    create_course_page.check_visible_exercise_title()

    # Проверить наличие кнопки создания задания
    create_course_page.check_visible_create_exercise_button()

    # Убедиться, что отображается блок с пустыми заданиями
    create_course_page.check_visible_exercises_empty_view()

    # Загрузить изображение для превью курса
    create_course_page.upload_preview_image(file='./testdata/files/image.png')

    # Убедиться, что блок загрузки изображения отображает состояние, когда картинка успешно загружена
    create_course_page.check_visible_image_upload_view(is_image_uploaded=True)

    # Заполнить форму создания курса значениями
    create_course_page.fill_create_course_form(
        title="Playwright",
        estimated_time="2 weeks",
        description="Playwright",
        max_score="100",
        min_score="10"
    )

    # Нажать на кнопку создания курса
    create_course_page.click_create_course_button()

    # Проверить наличие заголовка "Courses"
    courses_list_page.check_visible_courses_title()

    # Проверить наличие кнопки создания курса — метод
    courses_list_page.check_visible_create_course_button()

    # Проверить корректность отображаемых данных на карточке курса
    courses_list_page.check_visible_course_card(
        index=0,
        title='Playwright',
        max_score='100',
        min_score='10',
        estimated_time='2 weeks'
    )