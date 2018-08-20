# -*- coding: utf-8 -*-


import logging

# 设置日志等级
# logging.basicConfig(level=logging.DEBUG)

# 设置日志格式
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

# 设置日志时间
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"

# 设置日志等级以及输出文件
logging.basicConfig(filename='d:/my.log', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)


def log(level_name, msg):
    if level_name == 'info':
        logging.info(msg)
    elif level_name == 'debug':
        logging.debug(msg)
    elif level_name == 'warning':
        logging.warning(msg)
