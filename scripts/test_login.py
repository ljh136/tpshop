import os, sys
sys.path.append(os.getcwd())

import pytest

from base.base_driver import init_driver
from page.login_page import LoginPage
from base.base_yml import yml_data_with_filename_and_key


def data_with_key(key):
    return yml_data_with_filename_and_key("login_data", key)


class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.login_page = LoginPage(self.driver)

    # @pytest.mark.parametrize(("username", "password", "toast"), data_with_key("test_login"))
    # def test_login(self, username, password, toast):
    #     # 输入手机号
    #     self.login_page.input_username(username)
    #     # 输入密码
    #     self.login_page.input_password(password)
    #     # 点击登录
    #     self.login_page.click_login()
    #
    #     assert self.login_page.is_toast_exist(toast)

    @pytest.mark.parametrize("args", data_with_key("test_login"))
    def test_login(self, args):
        # 输入手机号
        self.login_page.input_username(args["username"])
        # 输入密码
        self.login_page.input_password(args["password"])
        # 点击登录
        self.login_page.click_login()

        assert self.login_page.is_toast_exist(args["toast"])

