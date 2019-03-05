from LetsCodeIt.Base.Base_driver import BaseDriver


class RegistrationPage(BaseDriver):
    url = "https://sso.teachable.com/secure/42299/checkout/342638/selenium-webdriver-with-python3?coupon_code=20ONLY"
    email_input = "//input[@type='email']"
    user_name = "//input[@name='username']"
    allow_email_check_box = "//input[@name='allow_instructor_emails' and @type='checkbox']"
    password = "//input[@type='password']"
    CC_nbr_frame = "//iframe[@name = '__privateStripeFrame4']"
    card_number_input = "//input[@aria-label='Credit or debit card number']"
    CC_exp_frame = "//iframe[@name='__privateStripeFrame5']"
    CC_exp_input ="//input[@name='exp-date']"
    CVV_frame = "//iframe[@name='__privateStripeFrame6']"
    CVV_input = "//input[@name='cvc']"
    confirm_button = "//button[@id='confirm-purchase']"



    def __init__(self, browser):
        super().__init__(browser)

    def load_page(self):
        self.driver.get(RegistrationPage.url)

    def enter_email(self, email):
        self.send_kyes_to_element(RegistrationPage.email_input, "xpath", email)

    def enter_name(self, name):
        self.send_kyes_to_element(RegistrationPage.user_name, "xpath", name)

    def enter_pass(self, password):
        self.send_kyes_to_element(RegistrationPage.password, "xpath", password)

    def enter_CC_nbr(self, cc_nbr):
        self.move_to_frame(RegistrationPage.CC_nbr_frame, "xpath")
        self.send_kyes_to_element(RegistrationPage.card_number_input, "xpath", cc_nbr)

        self.driver.switch_to.default_content()

    def enter_cc_exp(self, exp_MMYY):
        self.move_to_frame(RegistrationPage.CC_exp_frame, "xpath")
        self.send_kyes_to_element(RegistrationPage.CC_exp_input, "xpath", exp_MMYY)
        self.driver.switch_to.default_content()

    def enter_cvv_nbr(self, cvv):
        self.move_to_frame(RegistrationPage.CVV_frame, "xpath")
        self.send_kyes_to_element(RegistrationPage.CVV_input, "xpath", cvv)
        self.driver.switch_to.default_content()

    def click_confirm_purchase(self):
        self.click_element(RegistrationPage.confirm_button, "xpath")

