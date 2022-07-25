#coding = utf-8
from appium import webdriver


class HandleDriver:

    _driver = None
    caps = {
            "platformName": "android",
            "platformVersion": "7.1.2",
            "noReset": False,
            "autoGrantPermissions": True,
            "automationName": "Uiautomator2"
    }
    # 创建一个手机驱动器对象，如果已经存在，则不再创建，直接返回已存在的驱动器，保证自动化过程中同时只有一个驱动器
    # 如果不做这个判断，那么只要调用一次get_driver，就会创建一个驱动器对象
    @classmethod
    def get_driver(cls):
        if cls._driver == None:
            cls._driver = webdriver.Remote("127.0.0.1:4723/wd/hub", cls.caps)
        return cls._driver

    # 断开驱动器
    @classmethod
    def quit_driver(cls):
        if cls._driver != None:
            cls._driver.quit()
            cls._driver = None


if __name__ == '__main__':
    HandleDriver().get_driver().start_activity("com.uc108.mobile.gamecenter", ".accountmodule.ui.LoginActivity")



