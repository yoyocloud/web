#coding=utf-8
from selenium.webdriver.common.by import By
class LoginLocator:
    username_locator = (By.NAME, 'phone')
    pwd_locator = (By.XPATH, "// input[@name='password']")
    login_button=(By.XPATH,"//button[@class='btn btn-special']")
    mid_errmsg=(By.XPATH,"//div[@class='layui-layer-content']")
    down_errmsg=(By.XPATH,"//div[@class='form-error-info']")