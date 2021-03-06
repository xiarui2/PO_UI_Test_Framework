from selenium import webdriver
from element_infos.login_page import LoginPage
from selenium.webdriver.common.by import By
import time,os
from common.log_utils import logger
current_path = os.path.dirname(__file__)
driver_path = os.path.join(current_path,'../webdriver/chromedriver.exe')

class MainPage():  #类名————》页面
    def __init__(self):
        logon_page = LoginPage()
        logon_page.input_username('test01')
        logon_page.input_password('newdream123')
        logon_page.click_login()
        self.driver = logon_page.driver #把login_page的driver对象转移到mainpage里面来
        self.companyname_showbox = self.driver.find_element(By.CSS_SELECTOR,'h1#companyname')
        self.myzone_menu = self.driver.find_element(By.CSS_SELECTOR,'li[data-id="my"]')
        self.product_menu = self.driver.find_element(By.CSS_SELECTOR,'li[data-id="product"]')
        self.username_showspan = self.driver.find_element(By.CSS_SELECTOR,'span.user-name')

    def get_companyname(self):#获取公司名称
        value = self.companyname_showbox.get_attribute('title')
        return value
    def goto_myzon(self):   #进入我的地盘菜单
        self.myzone_menu.click()
    def goto_product(self):  #进入产品菜单
        self.product_menu.click()
    def get_username(self):
        value = self.username_showspan.text
        logger.info('获取用户名成功，用户名是：'+str(value))
        return value



if __name__ =="__main__":
    main_page = MainPage()
    username = main_page.get_username()
    print(username)
























