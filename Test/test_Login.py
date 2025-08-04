import pytest

from PageObject.signUp_signIn import signIn_up
from Utilities.utility import utility


class Test_Embibe_Login(utility):

#Git Upload/Push the code

    @pytest.mark.usefixtures("setup", "log_on_failure")
    def test_sign_in_password(self):
        login = signIn_up(self.driver)
        login.test_sign_in_password()
        log = self.getLogger()
        log.info("Testcase: Sign in with Password")

    @pytest.mark.usefixtures("setup", "log_on_failure")
    def test_signIn_mobile(self):
        log = self.getLogger()
        login = signIn_up(self.driver)
        login.sign_in_with_mobile()
        log.info("Testcase: Sign in with Mobile number")