import pytest
from selenium.webdriver import Chrome
from PageObjects.login_page import LoginPage
from TestDatas.login_data import url

driver=''
@pytest.fixture(scope="class")
def access_web():
    #前置条件
    #启动浏览器
    global driver
    driver=Chrome()
    #输入网址
    driver.get(url)
    #创建登录页面类的对象
    lp=LoginPage(driver)
    #
    yield (driver,lp)
    #
    # #后置条件
    # driver.quit()


#在每个函数执行完之后刷新页面，级别是函数级
@pytest.fixture()
def refresh_web():
    global driver
    driver.refresh()











@pytest.fixture()
def demo():
    print("-----这是function的开始")
    yield
    print("---------这是一个function的结束")
