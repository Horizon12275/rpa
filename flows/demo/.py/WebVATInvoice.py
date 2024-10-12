from datetime import datetime
from wsgiref.handlers import format_date_time
from time import mktime
import hashlib
import base64
import hmac
from urllib.parse import urlencode
import os
import traceback
import json
import requests

'''
增值税发票识别 WebAPI 接口调用示例
运行前：请先填写Appid、APIKey、APISecret以及图片路径
接口文档（必看）：https://www.xfyun.cn/doc/words/vat_invoice/API.html
'''


class AssembleHeaderException(Exception):
    def __init__(self, msg):
        self.message = msg


class Url:
    def __init__(this, host, path, schema):
        this.host = host
        this.path = path
        this.schema = schema
        pass


# calculate sha256 and encode to base64
def sha256base64(data):
    sha256 = hashlib.sha256()
    sha256.update(data)
    digest = base64.b64encode(sha256.digest()).decode(encoding='utf-8')
    return digest


def parse_url(requset_url):
    stidx = requset_url.index("://")
    host = requset_url[stidx + 3:]
    schema = requset_url[:stidx + 3]
    edidx = host.index("/")
    if edidx <= 0:
        raise AssembleHeaderException("invalid request url:" + requset_url)
    path = host[edidx:]
    host = host[:edidx]
    u = Url(host, path, schema)
    return u


# build websocket auth request url
def assemble_ws_auth_url(requset_url, method="POST", api_key="", api_secret=""):
    u = parse_url(requset_url)
    host = u.host
    path = u.path
    now = datetime.now()
    date = format_date_time(mktime(now.timetuple()))
    #print(date)
    # date = "Thu, 12 Dec 2019 01:57:27 GMT"
    signature_origin = "host: {}\ndate: {}\n{} {} HTTP/1.1".format(host, date, method, path)
    #print(signature_origin)
    signature_sha = hmac.new(api_secret.encode('utf-8'), signature_origin.encode('utf-8'),
                             digestmod=hashlib.sha256).digest()
    signature_sha = base64.b64encode(signature_sha).decode(encoding='utf-8')
    authorization_origin = "api_key=\"%s\", algorithm=\"%s\", headers=\"%s\", signature=\"%s\"" % (
        api_key, "hmac-sha256", "host date request-line", signature_sha)
    authorization = base64.b64encode(authorization_origin.encode('utf-8')).decode(encoding='utf-8')
    #print(authorization_origin)
    values = {
        "host": host,
        "date": date,
        "authorization": authorization
    }

    return requset_url + "?" + urlencode(values)


# 控制台获取以下信息
APPId = "5112a02c"
APISecret = "ZmFlMzE4ZmMzNmZjZWVjMThlZjBjOTMw"
APIKey = "bef4768fcf5354adab0085747446c91f"

pic_name = "a320"

with open(f'../../../dataset/a/{pic_name}.jpg', 'rb') as f:
    imageBytes = f.read()

url = 'http://api.xf-yun.com/v1/private/s824758f1'

body = {
    "header": {
        "app_id": APPId,
        "status": 3,
    },
    "parameter": {
        "s824758f1": {
            "template_list": "vat_invoice",
            "result": {
                "encoding": "utf8",
                "compress": "raw",
                "format": "json"
            }
        }
    },
    "payload": {
        "s824758f1_data_1": {
            "encoding": "jpg",
            "image": str(base64.b64encode(imageBytes), 'UTF-8'),
            "status": 3
        }
    }
}

request_url = assemble_ws_auth_url(url, "POST", APIKey, APISecret)

headers = {'content-type': "application/json", 'host': 'api.xf-yun.com', 'app_id': APPId}
#print(request_url)
response = requests.post(request_url, data=json.dumps(body), headers=headers)
# print(response)

# print(response.content)
# print("resp=>"+response.content.decode())
tempResult = json.loads(response.content.decode())
finalResult = base64.b64decode(tempResult['payload']['result']['text']).decode()
finalResult = finalResult.replace(" ", "").replace("\n", "").replace("\t", "").strip()
# print("text字段Base64解码后=>"+finalResult)

# 把finalResult写入json文件
with open(f'../../../dataset/result/{pic_name}.json', 'w') as f:
    f.write(finalResult)
    f.close()
