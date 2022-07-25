#coding=utf-8
import time
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utils.GetDriver import GetDriver
from selenium.webdriver.support.wait import WebDriverWait


driver = GetDriver().get_driver()
if driver.is_app_installed("com.uc108.mobile.gamecenter") == False:
    driver.install_app(r"C:\Users\Echo\Desktop\appiumiconapk\tongchengyouyxdt_v5.9.20_itmop.com.apk")
    time.sleep(10)
    driver.start_activity("com.uc108.mobile.gamecenter",".ui.SplashActivity")
    driver.find_element(By.XPATH,"//*[@text='同意']").click()
else:
    driver.start_activity("com.uc108.mobile.gamecenter",".accountmodule.ui.LoginActivity")
    time.sleep(1)
    try:
        ele = EC.visibility_of_element_located((By.XPATH,"//*[@text='同意']"))(driver)
        if ele:
            driver.find_element(By.XPATH,"//*[@text='同意']").click()
    except Exception as e:
        print("进入登录页面")




# driver.remove_app("com.uc108.mobile.gamecenter")
# driver.background_app(5)

driver.quit()