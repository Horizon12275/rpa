import requests
import time
import hashlib
import base64
import json
import os

URL = "http://webapi.xfyun.cn/v1/service/v1/ocr/invoice" # 请求地址 http[s]: //webapi.xfyun.cn/v1/service/v1/ocr/invoice
APPID = "5112a02c"  # 需要填入你的APPID
API_KEY = "7948ef3df76719739683e3d1cc391e0a"  # 需要填入你的API_KEY

def getHeader():
    curTime = str(int(time.time()))  # 获取当前时间戳
    param = {"engine_type": "invoice"}  # 设置OCR类型为发票识别
    param = json.dumps(param)  # 将参数转换为JSON字符串
    paramBase64 = base64.b64encode(param.encode('utf-8'))  # Base64编码参数

    # 构造校验字符串并生成MD5签名
    m2 = hashlib.md5() # 创建一个 md5 哈希对象
    str1 = API_KEY + curTime + str(paramBase64, 'utf-8')
    m2.update(str1.encode('utf-8')) # 更新哈希对象，添加需要计算哈希值的数据
    checkSum = m2.hexdigest() # 计算哈希值并获取其十六进制表示形式

    # 构造请求头
    header = {
        'X-CurTime': curTime,
        'X-Param': paramBase64,
        'X-Appid': APPID,
        'X-CheckSum': checkSum,
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
    }
    return header

# 遍历文件夹中的所有图片
def process_images_in_folder(folder_path):

    for file_name in os.listdir(folder_path):
        # 只处理图片文件（png、jpg、jpeg）
        if file_name.endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(folder_path, file_name)
            print(f"Processing {image_path}...")

            with open(image_path, 'rb') as f:
                image_data = f.read()

            # 将图片数据编码为Base64
            image_base64 = str(base64.b64encode(image_data), 'utf-8')

            # 准备请求数据
            data = {
                'image': image_base64
            }

            # 发送POST请求
            response = requests.post(URL, data=data, headers=getHeader())
            result = json.loads(response.content.decode('utf-8'))
            print(result)

# 指定包含图片的文件夹路径
image_folder = '../dataset_test'

# 处理文件夹中的所有图片并提取信息
process_images_in_folder(image_folder)
