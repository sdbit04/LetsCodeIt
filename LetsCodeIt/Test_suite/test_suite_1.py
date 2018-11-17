import unittest
from LetsCodeIt.Tests.test_course_page import TestCoursePage
from LetsCodeIt.Tests.test_registration_page import TestRegistrationPage

TL_object = unittest.TestLoader()
# Courses = TL_object.loadTestsFromTestCase(TestCoursePage)
Registration = TL_object.loadTestsFromTestCase(TestRegistrationPage)

# Create test suite
smoke_test = unittest.TestSuite([Registration])
unittest.TextTestRunner().run(smoke_test)
