#coding=utf-8
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import logging
import datetime
from Common.path_dir import screenshots_dir
import time


#1/封装基本函数---执行日志，异常处理，失败截图
#2/所有的页面公共部分，不是指业务
class BasePage:

    def __init__(self,driver):
        self.driver=driver

    #等待元素可见
    def wait_eleVisible(self,locator,times=30,poll_frequency=0.5,doc=''):
        '''
        :param locator:是元素定位表达式,元素形式(元素定位方式，元素定位表达式)
        :param times:等待时间，有默认值
        :param poll_frequency:轮询时间
        :param doc:是日志的详细描述
        :return:None
        '''
        logging.info("等待元素{}可见".format(locator))
        try:
            #开始等待的时间
            start_time=datetime.datetime.now()
            ele=WebDriverWait(self.driver,times,poll_frequency).until(ec.visibility_of_element_located(locator))
            #结束等待的时间
            end_time=datetime.datetime.now()
            #求差值，写在日志中，描述等待了多久
            time=start_time-end_time
            logging.info("等待时常为{}".format(time))
            return ele
        except:
            logging.exception("等待元素可见失败")
            self.save_screenshots(doc)
            raise



    #等待元素存在
    def wait_elePresence(self,locator,times=30,poll_frequency=0.5,doc=""):
        logging.info("等待元素存在")
        try:
            ele=WebDriverWait(self.driver,times,poll_frequency).until(ec.presence_of_element_located(locator))
            return ele
        except:
            logging.exception('等待元素存在失败')
            self.save_screenshots(doc)
            raise

    #查找元素
    def get_element(self,locator,doc=""):
        logging.info("查找元素：{}".format(locator))
        try:
            return self.driver.find_element(*locator)
        except:
            logging.exception("查找元素失败")
            self.save_screenshots(doc)
            raise

    #点击操作
    def click_element(self,locator,doc=''):
        #找元素
        ele=self.get_element(locator,doc)
        #元素操作
        logging.info("{0}页面，点击元素:{1}".format(doc,locator))
        try:
            ele.click()
        except:
            logging.exception("点击元素操作失败")
            self.save_screenshots(doc)
            raise

    #输入操作
    def input_text(self,locator,content,doc=''):
        #找元素
        ele=self.get_element(locator)
        #操作元素
        logging.info("在{0}页面，在{1}元素中输入".format(doc,locator))
        try:
            ele.send_keys(content)
        except:
            logging.exception("输入内容操作失败")
            self.save_screenshots(doc)
            raise
    #获取元素的文本内容
    def get_text(self,locator,doc):
        #找元素
        ele=self.get_element(locator)
        #操作元素
        logging.info("在{}页面，获取元素".format(doc))
        try:
            return ele.text
        except:
            logging.exception("获取元素文本内容失败")
            self.save_screenshots(doc)
            raise

    #读取元素的属性
    def get_attribute(self,locator,name,doc=''):
        '''
        :param locator: 元素的定位表达式
        :param name: 想要获取的属性名称
        :param doc: 有关日志截图的一些操作
        :return: 返回值为元素的属性
        '''
        #找元素
        ele=self.get_element(locator)
        #获取属性
        logging.info("{}读取元素属性操作".format(doc))
        try:
            attr=ele.get_attribute(name)
            return attr
        except:
            logging.exception("读取元素属性操作失败")
            self.save_screenshots(doc)
            raise

    #alert处理
    #iframe切换

    #上传操作
    def upload_file(self):
        pass
    #滚动条处理
    #窗口切换
    #截图
    def save_screenshots(self,doc=""):
        #图片名称：模块名称_页面名称_操作名称_年月日时分秒.png
        file_name="{0}_时间为{1}.png".format(doc,time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime()))
        pic_name=screenshots_dir+'/'+file_name
        self.driver.save_screenshot(pic_name)
        logging.info("截图成功，存放路径为{}".format(pic_name))

