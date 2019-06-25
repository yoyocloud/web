#coding=utf-8
from PageObjects.login_page import LoginPage
from TestDatas import login_data as ld
from PageObjects.home_page import HomePage as hp
import logging
#参数化和上下文管理
import pytest

@pytest.mark.usefixtures('access_web')
@pytest.mark.usefixtures('refresh_web')
class TestCase:
    #登录失败的用例从按钮下方获取断言的提示
    @pytest.mark.smoke
    @pytest.mark.parametrize('data',ld.user_down_error)
    def test_login_failDown(self,access_web,data):
        #调用po页面中的登录方法
        access_web[1].login(data["username"],data["pwd"])
        #断言
        try:
            assert access_web[1].get_errMsg_down()==data["expected"]
        except AssertionError as e:
            logging.exception()
            raise e


    #登录失败的用例从页面中间获取断言提示
    @pytest.mark.smoke
    @pytest.mark.parametrize('data',ld.user_mid_authorize)
    def test_login_failMid(self,access_web,data):
        #调用po页面中的登录方法
        access_web[1].login(data["username"],data["pwd"])
        #断言
        try:
            assert access_web[1].get_errMsg_middle()==data["expected"]
        except AssertionError as e:
            logging.exception()
            raise e

    @pytest.mark.smoke
    def test_login_success(self,access_web):
        access_web[1].login(ld.user_info_success["username"],ld.user_info_success["pwd"])
        #断言
        try:
            assert hp(access_web[0]).logoutButton()
        except AssertionError as e:
            logging.exception()
            raise e

@pytest.mark.smoke1
@pytest.mark.usefixtures("demo")
def test_demo():
    print("22222222222")
    assert False

