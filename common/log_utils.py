import os
import logging
import time
# from common.local_config import local_config

current_path = os.path.dirname(os.path.abspath(__file__))
log_output_path = os.path.join(current_path,'..','logs')

class LogUtils:
    def __init__(self,log_path=log_output_path):
        self.log_file_name = os.path.join(log_output_path,'api_test_%s.log'%time.strftime("%Y_%m_%d")) #加上时间是为了按天产生日志
        # print(self.log_file_name)  #E:\自动化\P16_KEY_WORD_API_TEST_FRAME\common\..\logs\api_test_2022_04_23.log
        self.logger = logging.getLogger('ApiTestLog')
        #self.logger.setLevel(10)
        self.logger.setLevel(10)   #讲日志级别改成可配置
        console_handle = logging.StreamHandler()
        file_hander = logging.FileHandler(self.log_file_name, 'a', encoding='utf-8')   #增加编码防止日志乱码
        formatter = logging.Formatter(("%(asctime)s %(name)s %(levelname)s %(message)s"))
        console_handle.setFormatter(formatter)
        file_hander.setFormatter(formatter)

        self.logger.addHandler(console_handle)
        self.logger.addHandler(file_hander)
        console_handle.close()  #防止打印日志重复
        file_hander.close()

    def get_logger(self):
        return self.logger

logger = LogUtils().get_logger()


if __name__=="__main__":
    #LogUtils()
    logger.info("封装好的日志 i")
    logger.warning("封装好的日志 w")
    logger.error("封装好的日志 e")

