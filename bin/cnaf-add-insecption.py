# -*- coding: utf-8 -*-


"""咪咕包月查询
Usage:
miguQuery <session> <class_id> <inputfile> <outputfile>
"""

from docopt import docopt
import requests
import json
import os
import time
from datetime import datetime

if __name__ == '__main__':
    # 将绑定交互参数
    arguments = docopt(__doc__)
    session = arguments['<session>']
    class_id = arguments['<class_id>']
    inputfile = arguments['<inputfile>']
    outputfile = arguments['<outputfile>']
    url = "http://inspection.cnaf.com/api/v1/sa/term/create"

    if os.path.isfile(inputfile) == False:
        print("找不到此文件:{}".format(inputfile))
        exit(0)
    if os.path.isfile(outputfile) == True:
        print("文件: {} 已经存在，请保存为另一个名字".format(outputfile))
        exit(0)

    headers = {"Cookie": "CNAF_SESSIONID_V2017={}".format(session)}
    a = datetime.now()
    with open(inputfile, mode='r', encoding='utf-8') as f:
        for line in f:
            # split()默认以空格分隔，此处根据文档中数据进行分隔
            time.sleep(1)
            data_str = {'classId': class_id, 'content': line}
            r = requests.post(url, data_str, headers=headers)
            print(r.text)
    b = datetime.now()
    # print("{}:{}".format(a, b))
    print('Cost {} seconds'.format((b - a).seconds))
