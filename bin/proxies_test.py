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


# proxies = {'http':'http://202.106.16.36:3128'}


proxies = {'http':'http://202.106.16.36:3128'}

def main():
    start_time = datetime.now()
    url = 'http://ipconfig.me'


    response = requests.get(url)
    json_text = response.text
    print(json_text)
    # json_dict = json.loads(json_text)['comments']

    #     # print(page)
    # page = 112
    # print(json_dict)





if __name__ == '__main__':
    main()


