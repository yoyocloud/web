from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from Common.basepage import BasePage


class LoginPage(BasePage):
    '''类封装定位元素'''
    userame_locator = (By.NAME, 'phone')
    pwd_locator = (By.XPATH, "// input[@name='password']")

    def __init__(self, driver):
        '''登入页面 .pageObject实际就是类封装形式'''
        self.driver = driver
        self.url = 'http://120.78.128.25:8765/Index/login.html'

    def login(self, username, pwd):
        # driver=Chrome()
        '''访问登入页面'''
        self.driver.get(self.url)

        '''定位用户输入框 和 密码输入框'''
        user_ele = self.get_user_info()
        pwd_ele = self.get_pwd_info()

        '''发送用户名和密码'''
        user_ele.send_keys(username)
        pwd_ele.send_keys(pwd)
        user_ele.submit()
        return self.driver

    def get_flash_info(self):
        '''获取错误信息'''
        flash_ele = self.wait_presence_ele((By.XPATH, "// div[@class='form-error-info']"))
        # flash_ele = WebDriverWait(self.driver, 20).until(
        #     ec.presence_of_element_located((By.XPATH, "// div[@class='form-error-info']")))
        return flash_ele

    def get_arlt_info(self):
        '''获取弹窗信息'''
        arlt_ele = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located((By.XPATH, "//div[@class='layui-layer-content']")))
        return arlt_ele

    def clear_user_info(self):  # 清空输入框
        self.clear_username()
        self.clear_pwd()

    def clear_username(self):
        '''清空用户名'''
        return self.get_user_info().clear()

    def clear_pwd(self):
        '''清空密码'''
        return self.get_pwd_info().clear()

    def get_user_info(self):
        '''定位用户名'''
        user_ele = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located(self.userame_locator))
        return user_ele

    def get_pwd_info(self):
        '''定位密码'''
        pwd_ele = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located(self.pwd_locator))
        return pwd_ele
