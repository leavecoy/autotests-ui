import pytest
import allure

from config import settings
from tools.allure.tags import AllureTag
from pages.courses.create_course_page import CreateCoursePage
from pages.courses.courses_list_page import CoursesListPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from allure_commons.types import Severity
from tools.routes import AppRoute

@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.COURSES, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.COURSES)
@allure.sub_suite(AllureStory.COURSES)
class TestCourses:
    @allure.title('Check displaying of empty courses list')
    @allure.severity(Severity.NORMAL)
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit(AppRoute.COURSES)

        # Проверяем навбар
        courses_list_page.navbar.check_visible(settings.test_user.username)

        # Проверяем сайдбар
        courses_list_page.sidebar.check_visible()

        # Проверяем наличие и корректное отображение заголовка страницы
        courses_list_page.toolbar_view.check_visible()

        # Проверяем, что при отсутствии курсов отображается соответствующий блок с сообщением об отсутствии результатов
        courses_list_page.check_visible_empty_view()

    @allure.title('Create course')
    @allure.severity(Severity.CRITICAL)
    def test_create_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
        create_course_page.visit(AppRoute.COURSES_CREATE)

        # Проверить наличие заголовка "Create course"
        create_course_page.create_course_toolbar.check_visible(is_create_course_disabled=True)

        # Убедиться, что отображается пустой блок для предпросмотра изображения
        create_course_page.image_upload_widget.check_visible()

        # Проверить, что блок загрузки изображения отображается в состоянии, когда картинка не выбрана — метод
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)

        # Проверить, что форма создания курса отображается и содержит значения по умолчанию
        create_course_page.create_course_form.check_visible(
            title='',
            estimated_time='',
            description='',
            max_score='0',
            min_score='0'
        )

        # Проверить наличие заголовка "Exercises"
        create_course_page.create_course_exercises_toolbar.check_visible_exercise_title()

        # Убедиться, что отображается блок с пустыми заданиями
        create_course_page.check_visible_exercises_empty_view()

        # Загрузить изображение для превью курса
        create_course_page.image_upload_widget.upload_preview_image(settings.test_data.image_png_file)

        # Убедиться, что блок загрузки изображения отображает состояние, когда картинка успешно загружена
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)

        # Заполнить форму создания курса значениями
        create_course_page.create_course_form.fill(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10"
        )

        # Нажать на кнопку создания курса
        create_course_page.create_course_toolbar.click_create_course_button()

        # Проверить наличие заголовка "Courses"
        courses_list_page.toolbar_view.check_visible()

        # Проверить корректность отображаемых данных на карточке курса
        courses_list_page.course_view.check_visible(
            index=0,
            title='Playwright',
            max_score='100',
            min_score='10',
            estimated_time='2 weeks'
        )

    @allure.title('Edit course')
    @allure.severity(Severity.NORMAL)
    def test_edit_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
        # Переход на страницу создания курса
        create_course_page.visit(AppRoute.COURSES_CREATE)

        # Заполнение формы валидными данными
        create_course_page.create_course_form.fill(
            title='UI Course',
            estimated_time='1h',
            description='Course about QA automation',
            max_score='10',
            min_score='1'
        )

        # Загрузка изображения
        create_course_page.image_upload_widget.upload_preview_image(settings.test_data.image_png_file)

        # Нажатие на кнопку создания курса
        create_course_page.create_course_toolbar.click_create_course_button()

        # Проверка, что на странице списка курсов появилась карточка созданного курса
        courses_list_page.course_view.check_visible(
            index=0,
            title='UI Course',
            max_score='10',
            min_score='1',
            estimated_time='1h'
        )

        # Переход в режим редактирования через меню карточки
        courses_list_page.course_view.menu.click_edit(index=0)

        # Изменение всех полей формы
        create_course_page.create_course_form.fill(
            title='Edited title',
            estimated_time='2h',
            description='Edited description',
            max_score='5',
            min_score='2'
        )

        # Сохранение изменений
        create_course_page.create_course_toolbar.click_create_course_button()

        # Проверка, что карточка курса обновилась и отображает новые данные
        courses_list_page.course_view.check_visible(
            index=0,
            title='Edited title',
            max_score='5',
            min_score='2',
            estimated_time='2h'
        )