#!/usr/bin/env python3
# -*-coding:utf-8 -*-
from sample.aipass_client import execute
from data import *
import os
import json

if __name__ == "__main__":

    response_list = []
    os.remove("data.json") if os.path.exists("data.json") else None

    def ocr(path, data_set, cnt=0):
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in sorted(filenames):
                file_path = os.path.join(dirpath, filename)
                response = execute(
                    request_url,
                    request_data(file_path, APP_list[cnt % len(APP_list)].APPId),
                    "POST",
                    APP_list[cnt % len(APP_list)].APPId,
                    APP_list[cnt % len(APP_list)].APIKey,
                    APP_list[cnt % len(APP_list)].APISecret,
                    response_list,
                )
                response["file_name"] = filename
                response["data_set"] = data_set  # 用于区分数据集
                response_list.append(response)
                cnt += 1  # 用于循环使用APP_list中的不同KEY

    # ocr("input/1", 1)
    # ocr("input/2", 2)
    ocr("input/test",1)

    with open("data.json", "a") as json_file:
        json.dump(response_list, json_file, ensure_ascii=False)
