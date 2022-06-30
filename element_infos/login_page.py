from selenium import webdriver
from selenium.webdriver.common.by import By
from common.log_uitls import logger
import time,os
current_path = os.path.dirname(__file__)
driver_path = os.path.join(current_path,'../webdriver/chromedriver.exe')

class LoginPage():  #类名————》页面
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.driver.implicitly_wait(10)
        self.driver.get('http://47.107.178.45/zentao/www/index.php?m=user&f=login')
        self.driver.maximize_window()
        self.username_inputbox = self.driver.find_element(By.CSS_SELECTOR,'input.form-control[name="account"]') #类属性——》页面上的控件
        self.password_inputbox = self.driver.find_element(By.CSS_SELECTOR,'input[name="password"]')
        self.login_button = self.driver.find_element(By.CSS_SELECTOR,'button.btn.btn-primary')
        self.keeplogin_checkbox = self.driver.find_element(By.CSS_SELECTOR,'input#keepLoginon')

    def input_username(self,username):  #方法——》控件的操作
        self.username_inputbox.send_keys(username)
        logger.info('用户名输入框输入：'+str(username))

    def input_password(self,password):
        self.password_inputbox.send_keys(password)
        logger.info('密码输入框输入：' + str(password))

    def click_login(self):
        self.login_button.click()
        logger.info('点击登录按钮')

if __name__ =="__main__":
    logon_page = LoginPage()
    logon_page.input_username('test01')
    logon_page.input_password('newdream123')
    logon_page.click_login()
