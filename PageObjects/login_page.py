from Common.basepage import BasePage
from PageLocators.login_locator import LoginLocator as loc
from TestDatas import login_data

class LoginPage(BasePage):
    phone=18684720553
    #正常登录操作
    def login(self,username,passwd):

        doc="登录页面_登录操作"
        # self.driver.wait_eleVisible(loc.username_locator,doc=doc)
        #输入用户名
        self.input_text(loc.username_locator,username,doc)
        #输入密码
        self.input_text(loc.pwd_locator,passwd,doc)
        #点击登录按钮
        self.click_element(loc.login_button,doc)

    #获取页面中间的错误提示
    def get_errMsg_middle(self):

        doc="登录页面_获取页面中间错误提示操作"
        #找元素
        self.wait_eleVisible(loc.mid_errmsg,doc=doc)
        #获取元素的文本内容
        return self.get_text(loc.mid_errmsg,doc=doc)

    #获取输入框下方的错误提示
    def get_errMsg_down(self):

        doc="登录页面_获取输入框下方错误提示的操作"
        #找元素
        self.wait_eleVisible(loc.down_errmsg,doc=doc)
        #获取元素的文本内容
        return self.get_text(loc.down_errmsg,doc=doc)

