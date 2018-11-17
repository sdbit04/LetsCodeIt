from LetsCodeIt.Pages.registration_page import RegistrationPage
import pytest
from unittest import TestCase
import time
from ddt import ddt, unpack, data
from LetsCodeIt.Utils.input_register_page import get_data


@ddt
class TestRegistrationPage(TestCase):

    @pytest.fixture(autouse=True)
    def create_page_object(self):
        self.reg_page_ob = RegistrationPage("chrome")


    # @data(("absadf@gmail.com", "swapna", 1232836274561244, 1223, 3433), ("asonai@gmail.com", "sonai", 1232812274341244, 1123, 3435))
    @data(*(get_data()))
    @unpack
    def test_registration(self, email, user_name, cc_nbr, cc_exp, cvc):
        self.reg_page_ob.load_page()
        self.reg_page_ob.enter_email(email)
        self.reg_page_ob.enter_name(user_name)
        time.sleep(2)
        self.reg_page_ob.enter_CC_nbr(cc_nbr)
        time.sleep(0)
        self.reg_page_ob.enter_cc_exp(cc_exp)
        time.sleep(0)
        self.reg_page_ob.enter_cvv_nbr(cvc)
        time.sleep(2)
        self.reg_page_ob.driver.close()

