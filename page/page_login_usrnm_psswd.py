from selenium.webdriver.common.by import By

from base.base_element import BaseElement
from base.base_handle import BaseHandle


class ElementLayer(BaseElement):
    def __init__(self):
        super().__init__()
        self.loc_usernameEt = By.ID,"com.uc108.mobile.gamecenter:id/usernameEt"
        self.loc_passwordEt = By.ID,"com.uc108.mobile.gamecenter:id/passwordEt"
        self.loc_loginBtn = By.ID,"com.uc108.mobile.gamecenter:id/loginBtn"
        self.loc_forgetPasswordTv = By.ID,"com.uc108.mobile.gamecenter:id/forgetPasswordTv"
        self.loc_toast = By.XPATH, "//*[@class='android.widget.Toast']"

    def find_usernameEt(self):
        return self.get_element(self.loc_usernameEt)

    def find_passwordEt(self):
        return self.get_element(self.loc_passwordEt)

    def find_loginBtn(self):
        return self.get_element(self.loc_loginBtn)

    def find_forgetPasswordTv(self):
        return self.get_element(self.loc_forgetPasswordTv)

    def find_toast(self):
        return self.get_toast(self.loc_toast)


class HandleLayer(BaseHandle):
    def __init__(self):
        self.ele = ElementLayer()

    def input_username(self,username):
        self.input_text(self.ele.find_usernameEt(),username)

    def input_password(self,password):
        self.input_text(self.ele.find_passwordEt(),password)

    def click_loginBtn(self):
        self.ele.find_loginBtn().click()

    def click_forgetPasswordTv(self):
        self.ele.find_forgetPasswordTv().click()

    # 获取toast的显示消息
    def get_toast_message(self):
        message = self.get_toast_text(self.ele.find_toast())
        return message


class ProxyLoginUsrnmPsswdPage:
    def __init__(self):
        self.handle = HandleLayer()

    # 业务：输入用户名密码，点击登录
    def proxy_login_by_username_password(self,username,password):
        self.handle.input_username(username)
        self.handle.input_password(password)
        self.handle.click_loginBtn()

    # 业务：点击忘记密码
    def proxy_forgetpassword(self):
        self.handle.click_forgetPasswordTv()

    # 业务：获取toast消息
    def proxy_get_toast_message(self):
        return self.handle.get_toast_message()


