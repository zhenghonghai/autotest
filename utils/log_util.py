import logging
import os
import time
from utils.config_util import get_file_path


class Logger:

    def __init__(self):
        # 定义日志位置和文件名
        self.log_name = os.path.join(get_file_path('log'), "{}.log".format(time.strftime("%Y-%m-%d")))
        # 定义一个日志容器
        self.logger = logging.getLogger('log')
        # 设置日志打印的级别
        self.logger.setLevel(logging.DEBUG)
        # 创建日志输入的格式
        self.formatter = logging.Formatter('[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]: %(message)s')
        # 创建日志处理器，用来存放日志文件
        self.file_logger = logging.FileHandler(self.log_name, mode='a', encoding='utf8')
        # 创建日志处理器，在控制台打印
        self.console = logging.StreamHandler()
        # 设置控制台打印日志级别
        self.console.setLevel(logging.DEBUG)
        # 控制台打印日志格式
        self.console.setFormatter(self.formatter)
        # 文件存放日志级别
        self.file_logger.setLevel(logging.DEBUG)
        # 文件打印日志格式
        self.file_logger.setFormatter(self.formatter)
        # 将日志输出渠道添加到日志收集器中
        self.logger.addHandler(self.file_logger)
        self.logger.addHandler(self.console)
