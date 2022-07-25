import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.handle_driver import HandleDriver


class StartTcyApp:
    # 获取手机驱动器对象
    def __init__(self):
        self.driver = HandleDriver().get_driver()
    # 判断同城游是否已经安装，已安装返回True
    def tcyapp_is_install(self):
        return self.driver.install_app("com.uc108.mobile.gamecenter")
    # 打开同城游app,
    def start_tcyapp(self):
        #如果同城游已经安装，打开同城游，进入手机登录页，如果跳出授权，则点击授权
        if self.tcyapp_is_install():
            self.driver.start_activity("com.uc108.mobile.gamecenter",".accountmodule.ui.LoginActivity")
            try:
                ele = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, "//*[@text='同意']")))
                if ele:
                    self.driver.find_element(By.XPATH, "//*[@text='同意']").click()
            except Exception as e:
                print("已经点击过授权")
        #如果同城游没有安装，安装后打开，点击授权，使rootviewcontroller变为手机登录页
        else:
            self.driver.install_app(r"C:\Users\Echo\Desktop\appiumiconapk\tongchengyouyxdt_v5.9.20_itmop.com.apk")
            time.sleep(10)
            self.driver.start_activity("com.uc108.mobile.gamecenter", ".ui.SplashActivity")
            self.driver.find_element(By.XPATH, "//*[@text='同意']").click()

