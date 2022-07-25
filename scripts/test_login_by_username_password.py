import pytest

from page.page_login_input_phoneNum import ProxyLoginPhoneNumPage
from page.page_login_usrnm_psswd import ProxyLoginUsrnmPsswdPage
from utils.handle_driver import HandleDriver
from utils.start_tcyapp import StartTcyApp
from utils.handle_json import HandleJson

# 获取测试数据
case_data = HandleJson().get_case_values("login_by_username_password_data.json")
# 创建手机登录页业务层对象
class TestLoginByUsernamePassword:
    def setup_class(self):
        # 打开同城游app
        # StartTcyApp().start_tcyapp()
        HandleDriver().get_driver().start_activity("com.uc108.mobile.gamecenter", ".accountmodule.ui.LoginActivity")
        # 点击账号登录
        ProxyLoginPhoneNumPage().proxy_click_duanxin()

    def teardown_class(self):
        HandleDriver().quit_driver()

    @pytest.mark.parametrize("username,password,expect",case_data)
    def test_login(self,username,password,expect):
        ProxyLoginUsrnmPsswdPage().proxy_login_by_username_password(username,password)
        assert expect in ProxyLoginUsrnmPsswdPage().proxy_get_toast_message()

