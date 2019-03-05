import pytest
from LetsCodeIt.Pages.course_page import CoursePage
import time


class TestCoursePage():

    @pytest.fixture(autouse=True)
    def create_object_course_page(self):
        self.course_page = CoursePage(browser='chrome')  # Hard coded

    def test_page_load(self):
        self.course_page.load_page()
        self.course_page.take_screen_shot("FailedToFindElementCourse")
        time.sleep(2)
        self.course_page.driver.close()
        assert True

    @pytest.mark.skip()
    def test_opening_of_python_course(self):
        self.course_page.load_page()
        time.sleep(10)
        """
        driver.switchTo().frame() has multiple overloads.
        driver.switchTo().frame(name_or_id) 
        Here your iframe doesn't have id or name, so not for you.

        driver.switchTo().frame(index) 
        This is the last option to choose, because using index is not stable enough as you could imagine. If this is your only iframe in the page, try driver.switchTo().frame(0)

        driver.switchTo().frame(iframe_element) 
        The most common one. You locate your iframe like other elements, then pass it into the method.
        """

        self.course_page.move_to_courses_iframe()

        self.course_page.click_on_selenium_python()
        time.sleep(5)
        result = self.course_page.validate_if_selenium_python_open()
        assert result, True

    @pytest.mark.skip()
    def test_quit(self):
        self.course_page.driver.quit()

    @pytest.mark.skip()
    def test_2(self):
        assert 2 == 3
