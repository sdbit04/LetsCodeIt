from LetsCodeIt.Base.Base_driver import BaseDriver
import time


class CoursePage(BaseDriver):
    # Following are some class specific attributes, doesn't depends on browser type
    url = "http://www.letskodeit.com/courses"
    selenium_python = "//div[contains(text(), 'this course covers all the necessary topics including Python')]"
    welcome2selenium_python_course = "//h1[@class='course-title' and contains(text(), 'Selenium WebDriver With Python)]"
    iframe_courses_xpath = "//iframe[@id='i8y4laiuiframe']"

#   some elements of register page
    Enroll_button = "//*[@id='enroll-button-top']"
    email_input = "//input[@type='email']"
    user_name = "//input[@name='username']"
    allow_email_check_box = "//input[@name='allow_instructor_emails' and @type='checkbox']"
    password = "//input[@type='password']"

    def __init__(self, browser):
        super().__init__(browser=browser)

    def load_page(self):
        self.driver.get(url=CoursePage.url)

    def move_to_courses_iframe(self):
        element = self.wait_n_get_element(CoursePage.iframe_courses_xpath, 'xpath')
        self.driver.switch_to.frame(element)

    def click_on_selenium_python(self):
        self.wait_n_click_element(locator_type='xpath', locator=CoursePage.selenium_python)

    def validate_if_selenium_python_open(self):
        return self.validate_element_present(CoursePage.welcome2selenium_python_course, 'xpath')

    def click_enroll_button(self):
        """
        This method is for next to Courses page i.e welcome to course page
        :return:
        """
        # self.click_element(CoursePage.Enroll_button, 'xpath')
        self.wait_n_click_element(CoursePage.Enroll_button, 'xpath')

    def enter_email_id(self, new_email_id):
        """
        This method is for Enrolment to course page
        :return:
        """
        self.send_kyes_to_element(CoursePage.email_input, 'xpath', new_email_id)

    def enter_user_name(self, new_name):
        """
        This method is for Enrolment to course page
        :return:
        """
        self.send_kyes_to_element(CoursePage.user_name, 'xpath', new_name)

    def click_allow_email_checkbox(self):
        """
        This method is for Enrolment to course page
        :return:
        """
        self.wait_n_click_element(CoursePage.allow_email_check_box, 'xpath')

    def enter_password(self, password):
        self.wait_n_send_keys(CoursePage.password, 'xpath', password)


