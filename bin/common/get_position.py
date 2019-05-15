# -*- coding: utf-8 -*-
"""
根据图片取得文字坐标，需要注意图片识别坐标的原点在左下角（不是我们平时的左个角）
"""

import os
from common import log_tools


def recognition_img_txt(img_name):
    """
    将图片中文件识别出来

    """
    img_path = '..\\file\\{}'.format(img_name)
    # print(img_path)
    if os.path.isfile(img_path):
        recognition_str = 'tesseract {} out -l chi_sim makebox'.format(img_path)
        os.system(recognition_str)
        log_tools.log('info', recognition_str)
        log_tools.log('info', "输出坐标文件 out.box")
    else:
        log_tools.log('info', "{} not found.".format(img_name))


def get_position(str, img_name):
    """
    根据文字获取需要点击坐标
    """
    recognition_img_txt(img_name)
    list_word = []
    if os.path.isfile('out.box'):
        with open('out.box', encoding="utf8") as f:
            for line in f:
                if line.split()[0] in str:
                    list_word.append(line.split())
    return list_word


def get_position_only_str(str):
    list = []
    if os.path.isfile('out.box'):
        with open('out.box', encoding="utf8") as f:
            for line in f:
                if line.split()[0] in str:
                    list.append(line.split())
    return list



if __name__ == '__main__':
    # print(os.getcwd())
    print(get_position("云闪付", "..\\..\\file\\yun.png"))