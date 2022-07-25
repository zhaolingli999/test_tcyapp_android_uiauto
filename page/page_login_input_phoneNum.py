#coding=utf-8
from selenium.webdriver.common.by import By
from utils.handle_driver import HandleDriver
from base.base_element import BaseElement
from base.base_handle import BaseHandle

# 元素定位
class ElementLayer(BaseElement):
    def __init__(self):
        # 父类的初始化方法中是驱动器属性，子类重写了父类的初始化方法，如果不用super()引入，子类的属性中会没有driver属性，就不能self.driver调用驱动器
        super().__init__()
        # self.driver.start_activity("com.uc108.mobile.gamecenter", ".accountmodule.ui.LoginActivity")
        # 各个元素的定位器
        self.loc_et_phoneNum = By.ID,"com.uc108.mobile.gamecenter:id/et_phoneNum"
        self.loc_btn_next = By.ID,"com.uc108.mobile.gamecenter:id/btn_next"
        self.loc_igv_login_duanxin = By.ID,"com.uc108.mobile.gamecenter:id/igv_login_duanxin"
        self.loc_igv_login_weixin = By.ID,"com.uc108.mobile.gamecenter:id/igv_login_weixin"
        self.loc_igv_login_qq = By.ID,"com.uc108.mobile.gamecenter:id/igv_login_qq"
        self.loc_feedback = By.ID,"com.uc108.mobile.gamecenter:id/tv_firstlogin_feedback"
        self.loc_cb_agreeprivacy = By.ID,"com.uc108.mobile.gamecenter:id/cb_agreeprivacy"

    # 定位输入手机号编辑框
    def find_et_phoneNum(self):
        return self.get_element(self.loc_et_phoneNum)

    # 定位下一步按钮
    def find_btn_next(self):
        return self.get_element(self.loc_btn_next)

    # 定位账号登录入口
    def find_igv_login_duanxin(self):
        return self.get_element(self.loc_igv_login_duanxin)


# 元素操作
class HandleLayer(BaseHandle):
    def __init__(self):
        # 对元素进行操作，先创建一个元素层对象，来引用定位元素的方法
        self.ele = ElementLayer()

    # 输入框元素中输入内容
    def input_et_phoneNum(self,text):
        self.input_text(self.ele.find_et_phoneNum(),text)

    # 点击下一步元素
    def click_btn_next(self):
        self.ele.find_btn_next().click()

    # 点击账号登录入口按钮
    def click_igv_login_duanxin(self):
        self.ele.find_igv_login_duanxin().click()


# 业务层
class ProxyLoginPhoneNumPage:
    def __init__(self):
        # 创建操作层对象，调用操作层方法组装成业务
        self.handle_ele = HandleLayer()

    # 业务场景：输入手机号码，点击下一步操作
    def proxy_input_phoneNum(self,text):

        self.handle_ele.input_et_phoneNum(text)
        self.handle_ele.click_btn_next()

    # 业务场景：点击账号登录
    def proxy_click_duanxin(self):
        self.handle_ele.click_igv_login_duanxin()


if __name__ == '__main__':
    HandleDriver().get_driver().start_activity("com.uc108.mobile.gamecenter",".accountmodule.ui.LoginActivity")
    ProxyLoginPhoneNumPage().proxy_input_phoneNum("13444444444")








