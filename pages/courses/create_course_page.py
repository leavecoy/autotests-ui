from compontents.courses.create_course_exercise_form_component import CreateCourseExerciseFormComponent
from compontents.courses.create_course_toolbar_view_component import CreateCourseToolbarViewComponent
from compontents.navigation.navbar_component import NavbarComponent
from compontents.views.empty_view_component import EmptyViewComponent
from compontents.views.image_upload_widget_component import ImageUploadWidgetComponent
from compontents.courses.create_course_form_component import CreateCourseFormComponent
from compontents.courses.create_course_exercises_toolbar_view_component import CreateCourseExercisesToolbarViewComponent
from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.exercises_empty_view = EmptyViewComponent(page, identifier='create-course-exercises')
        self.image_upload_widget = ImageUploadWidgetComponent(page, identifier='create-course-preview')
        self.create_course_form = CreateCourseFormComponent(page)
        self.create_course_exercises_form = CreateCourseExerciseFormComponent(page)
        self.create_course_exercises_toolbar = CreateCourseExercisesToolbarViewComponent(page)
        self.create_course_toolbar = CreateCourseToolbarViewComponent(page)

    def check_visible_exercises_empty_view(self):
        self.exercises_empty_view.check_visible(
            title='There is no exercises',
            description='Click on "Create exercise" button to create new exercise'
        )

