from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Common.basepage import BasePage
from PageLocators.home_locator import homeLocator as hl


class HomePage(BasePage):
    '''登录成功后的首页类'''

    def logoutButton(self):
        doc="首页_退出"
        self.wait_eleVisible(hl.logout_button,doc=doc)
        try:
            self.get_text(hl.logout_button,doc)
            return True
        except:
            return False
            raise



