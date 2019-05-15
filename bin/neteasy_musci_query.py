import aiohttp
import asyncio
from Crypto.Cipher import AES
import base64
import rsa
import requests
import json
import random
import time
from math import floor
import os, sys
from datetime import datetime

#初始化
# proxyUrl = "http://202.106.16.36:3128"
#request headers,这些信息可以在ntesdoor日志request header中找到，copy过来就行
headers = {
    'Accept': "*/*",
    'Accept-Language': "zh-CN,zh;q=0.9",
    'Connection': "keep-alive",
    'Host': "music.163.com",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
    'Cookie':"_iuqxldmzr_=32; _ntes_nnid=09573c23cbaf950b7694066ccf35fc3e,1550223436864; _ntes_nuid=09573c23cbaf950b7694066ccf35fc3e; WM_TID=YO78QtDTZ05EBRABVBN51boVlSU0xIR9; JSESSIONID-WYYY=teUDtcpyxrHygf5QJQbXSClcBhrvng5XBQYQHE%5COFS91FpoqHmo6qX6FWHYeNHXkxIa8SFtyRKiCu6WIQkEOlyr135%2Bcp9QrdVadp53Aq0cp6NdPVVvFhhhlm%5CzJhAoiCemnaIVgd%5Cmy7om0Q7t5ikjNbehR1yJ3jZe6jM%5CsTYR%5C851N%3A1550813823028; WM_NI=hp4wihrI%2Bbhh9YyL8RNRfLSY%2BBAqE18jno67ha79nbt0eoZCwySRDnitIz3Kwi4f6VqmivvbXa2BeNCv1CmsKBBFOd6MWIdfepCci9diULyt55t8b1kPOnAU%2FpLfdiLsN2U%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed4c866f690feb1bc4588868ea7d15b869a9eabf368f493aad1b747a593bcb5c72af0fea7c3b92aacb0fc98ec64b297e583eb64fb87b7adbb5a8e8eaaadd253e99e8f92c83bfcb6a290b53dacbff9daed6ab8f0ab90d949b5a79db3c766abac879bb241b5b7fc87b55eb3b3a797f56a9cbffea3e84681aaffa4f079899e8ea7ce70f69399aae76ea7b08d84ec33a8b79badfc80f7ebbcd9e13ba990818fc45fedb08487e76390ad82d3d837e2a3"
 }
proxies = {'http':'http://202.106.16.36:3128'}
# proxies = {'http':'http://119.57.108.65:53281'}




first_param = "{rid:\"\", offset:\"0\", total:\"true\", limit:\"20\", csrf_token:\"\"}"
second_param = "010001"
third_param = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
forth_param = "0CoJUm6Qyw8W8jud"


def get_params(i):
    if i == 0:
        first_param = '{rid:"", offset:"0", total:"true", limit:"20", csrf_token:""}'
    else:
        offset = str(i * 20)
        first_param = '{rid:"", offset:"%s", total:"%s", limit:"20", csrf_token:""}' % (offset, 'flase')
    iv = "0102030405060708"
    first_key = forth_param
    second_key = 16 * 'F'
    h_encText = AES_encrypt(first_param, first_key, iv)
    #h_encText为bytes要转成str后在AES_encrypt方法中才能正常添加空格
    h_encText = AES_encrypt(bytes.decode(h_encText), second_key, iv)
    return h_encText


def AES_encrypt(text, key, iv):
    pad = 16 - len(text) % 16
    text = text + pad * chr(pad)
    encryptor = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
    encrypt_text = encryptor.encrypt(text.encode('utf-8'))
    encrypt_text = base64.b64encode(encrypt_text)
    return encrypt_text


def get_encSecKey():
    encSecKey = '257348aecb5e556c066de214e531faadd1c55d814f9be95fd06d6bff9f4c7a41f831f6394d5a3fd2e3881736d94a02ca919d952872e7d0a50ebfa1769a7a62d512f5f1ca21aec60bc3819a9c3ffca5eca9a0dba6d6f7249b06f5965ecfff3695b54e1c28f3f624750ed39e7de08fc8493242e26dbc4484a01c76f739e135637c'
    return encSecKey

def get_json(url, params, encSecKey):
    data = {
        "params": params,
        "encSecKey": encSecKey
    }
    response = requests.post(url, headers=headers, data=data, proxies = proxies)
    return response.content

def get_page(url):
    params = get_params(0);
    encSecKey = get_encSecKey();
    json_text = get_json(url, params, encSecKey)
    json_dict = json.loads(json_text)
    total_comment = json_dict['total']
    page=floor((total_comment/20))+1
    print('***查询到评论共计{}条,{}页***'.format(total_comment,page))
    return page

def main():
    start_time = datetime.now()
    url = 'https://music.163.com/weapi/v1/resource/comments/R_SO_4_29004400?csrf_token='

    # json_text = get_json(url, get_params(112), get_encSecKey())
    # print(json_text)
    # json_dict = json.loads(json_text)['comments']
    # print(json_dict)
    #     # print(page)
    # page = 112


    page = get_page(url)
    outputfile = "D:/netEasy_music_spider.txt"
    if os.path.isfile(outputfile) == True:
        print("文件: {} 已经存在，请保存为另一个名字".format(outputfile))
        exit(0)
    with open(outputfile, mode='w', encoding='utf-8') as file:

        for i in range(page):
            params = get_params(i);
            encSecKey = get_encSecKey();
            json_text = get_json(url, params, encSecKey)
            # print(json.loads(json_text))
            json_dict = json.loads(json_text)['comments']
            for j in range(len(json_dict)):
                time_local = time.localtime(int(json_dict[j]['time'] / 1000))  # 将毫秒级时间转换为日期
                dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
                # print("用户名："+ json_dict[j]['user']['nickname'])
                # print("时间：" + dt)
                # print("评论：" + json_dict[j]['content'])
                # print("--------")

                file.write('用户名：{}\n'.format(json_dict[j]['user']['nickname']))
                file.write('时间：{}\n'.format(dt))
                file.write('评论：{}\n'.format(json_dict[j]['content']))
                file.write('------------------------\n')
            time.sleep(random.uniform(0.2, 0.5))
            print("抓取完第{}页".format(i))
    end_time = datetime.now()
    print(start_time)
    print(end_time)




if __name__ == '__main__':
    main()



#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(fetch())