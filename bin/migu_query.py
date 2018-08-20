# -*- coding: utf-8 -*-


"""咪咕包月查询
Usage:
miguQuery <session> <inputfile> <outputfile>
"""

from docopt import docopt
import aiohttp
import asyncio
import sys
import os
import aiofiles
from datetime import datetime
from time import time
import json


async def fetch_test(url, jsession_id):
    async with aiohttp.ClientSession(headers={"Cookie": "JSESSIONID={}".format(jsession_id)}) as session:
        async with session.get(url) as resp:
            return await resp.read()


async def fetch(url, session, sem):
    async with sem:
        async with session.get(url) as resp:
            # 不加下面这一行的话，不会实现协程异步
            await asyncio.sleep(0)
            return await resp.read()


async def run(url, jsession_id, inputfile, outputfile):
    tasks = []
    numbers = []
    count = 0
    # 脚本名：sys.argv[0],参数1：sys.argv[1],参数2：sys.argv[2]
    # file = sys.argv[1]
    file = inputfile
    # 会报：concurrent.futures._base.TimeoutError原因为：Once it's a big number such as 30,000 it can't be physically done within 10 seconds due to networks/ram/cpu capacity.所以需要限制携程的信号量
    sem = asyncio.Semaphore(1000)
    # 将session以参数传入fetch中，让所有请求只使用一个session，而不用每个请求都创建一个session
    async with aiohttp.ClientSession(headers={"Cookie": "JSESSIONID={}".format(jsession_id)}) as session:
        with open(file, mode='r') as f:
            for line in f:
                # split()默认以空格分隔，此处根据文档中数据进行分隔
                phone_number = line.strip()
                numbers.append(phone_number)
                # print(url.format(phone_number))
                # task = asyncio.ensure_future(fetch(url.format(phoneNumber), jssessionId))
                task = fetch(url.format(phone_number), session, sem)
                tasks.append(task)

        ##它搜集所有的Future对象，然后等待他们返回
        responses = await asyncio.gather(*tasks)
        file = open(outputfile, 'w')
        for j in range(len(responses)):
            res_json = json.loads(responses[j].decode('utf-8'))
            if res_json["reDesc"] != "[FCMG]操作成功":
                # print('{}:{}'.format(numbers[j],responses[j].decode('utf-8')))
                file.write('{}:{}\n'.format(numbers[j], responses[j].decode('utf-8')))
                count += 1
        file.close()
        print("总计查询到包月号码:{}个".format(count))
        print("查询结果输出到:{}".format(outputfile))


# if __name__ == '__main__':
#     # 将绑定交互参数
#     arguments = docopt(__doc__)
#     session = arguments['<session>']
#     inputfile = arguments['<inputfile>']
#     outputfile = arguments['<outputfile>']
#     url = "http://211.137.107.18:8888/cm/user!queryMonthInfoByMsisdn.action?msisdn={}&serviceType=B"
#
#     if os.path.isfile(inputfile) == False:
#         print("找不到此文件:{}".format(inputfile))
#         exit(0)
#     if os.path.isfile(outputfile) == True:
#         print("文件: {} 已经存在，请保存为另一个名字".format(outputfile))
#         exit(0)
#
#     # 创建一个asyncio loop的实例， 然后将任务加入其中
#     loop = asyncio.get_event_loop()
#     resp = loop.run_until_complete(fetch_test(url.format('13666198249'), session)).decode('utf-8')
#     if 'login.jsp' in resp:
#         print("当前session:{} 不正确或已过期，请重新传入session参数".format(session))
#         loop.close()
#         exit(0)
#
#     a = datetime.now()
#     loop.run_until_complete(run(url, session, inputfile, outputfile))
#     loop.close()
#     b = datetime.now()
#     # print("{}:{}".format(a, b))
#     print('Cost {} seconds'.format((b - a).seconds))

if __name__ == '__main__':
    # 将绑定交互参数
    arguments = docopt(__doc__)
    session = arguments['<session>']
    inputfile = arguments['<inputfile>']
    outputfile = arguments['<outputfile>']
    url = "http://211.137.107.18:8888/cm/user!queryMonthInfoByMsisdn.action?msisdn={}&serviceType=B"

    if os.path.isfile(inputfile) == False:
        print("找不到此文件:{}".format(inputfile))
        exit(0)
    if os.path.isfile(outputfile) == True:
        print("文件: {} 已经存在，请保存为另一个名字".format(outputfile))
        exit(0)

    # 创建一个asyncio loop的实例， 然后将任务加入其中
    loop = asyncio.get_event_loop()
    resp = loop.run_until_complete(fetch_test(url.format('13666198249'), session)).decode('utf-8')
    if 'login.jsp' in resp:
        print("当前session:{} 不正确或已过期，请重新传入session参数".format(session))
        loop.close()
        exit(0)

    a = datetime.now()
    loop.run_until_complete(run(url, session, inputfile, outputfile))
    loop.close()
    b = datetime.now()
    # print("{}:{}".format(a, b))
    print('Cost {} seconds'.format((b - a).seconds))
