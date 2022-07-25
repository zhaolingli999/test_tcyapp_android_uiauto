#coding=utf-8
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils.handle_driver import HandleDriver


class BaseElement():
    """
    定位元素的基类
    对象库层基类
    所有对元素的定位都需要用到驱动器对象
    """
    # 初始化
    def __init__(self):
        # 获取一个驱动器对象
        self.driver = HandleDriver.get_driver()


    def get_element(self,locator):
        """
        通过显式等待来定位普通元素
        :param locator: 元素的定位器
        :return: 元素
        """
        wait = WebDriverWait(self.driver,10)
        # 元素存在并可见，则返回该元素
        # ele = wait.until(EC.visibility_of_element_located(locator))
        ele = wait.until(lambda x:x.find_element(*locator))
        return ele

    def get_toast(self,locator):
        """
        通过显示等待来定位toast元素
        :param locator: 传进来的定位器，建议：locator=(By.XPATH, "//*[@class='android.widget.Toast']")
        :return: toast元素
        """
        wait = WebDriverWait(self.driver, 10)
        # ele = wait.until(EC.presence_of_element_located((By.XPATH,"//*[@text={}]".format(message))))
        # ele = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@class='android.widget.Toast']")))
        ele = wait.until(EC.presence_of_element_located(locator))
        return ele

if __name__ == '__main__':
    HandleDriver().get_driver().start_activity("com.uc108.mobile.gamecenter", ".accountmodule.ui.LoginActivity")
    time.sleep(3)
    BaseElement().get_element((By.ID,"com.uc108.mobile.gamecenter:id/btn_next")).click()