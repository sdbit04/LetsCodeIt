from LetsCodeIt.Base.Base_driver import BaseDriver


class ContinuousAssertion(BaseDriver):

    def __init__(self, browser):
        super().__init__(browser=browser)
        self.result_set = []

    def store_result(self):
        pass

    def final_result(self):
        pass
