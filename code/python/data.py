class APP:
    def __init__(self, APPId: str, APIKey: str, APISecret: str):
        self.APPId = APPId
        self.APIKey = APIKey
        self.APISecret = APISecret


# 创建 APP 实例并存储在列表中
APP_list = [
    APP(
        APPId="5fb8d78a",
        APIKey="8dca7165cff031a03e634121a3469261",
        APISecret="NTllNmU5YmJjZmEwZGUwNTdlYzg5Njg3",
    ),
    APP(
        APPId="5112a02c",
        APIKey="bef4768fcf5354adab0085747446c91f",
        APISecret="ZmFlMzE4ZmMzNmZjZWVjMThlZjBjOTMw",
    ),
    APP(
        APPId="99c5b6a4",
        APIKey="dd0a0077ca5520d0fc21b0665092c526",
        APISecret="MmYzNTEwOGFjMjA4ZWIyOGJlYTUzMmE1",
    ),
]


# 请求数据
def request_data(image_path, APPId):
    return {
        "header": {"app_id": APPId, "status": 3},
        "parameter": {
            "image_recognize": {
                "output_text_result": {
                    "encoding": "utf8",
                    "compress": "raw",
                    "format": "plain",
                }
            }
        },
        "payload": {"image": {"encoding": "png", "image": image_path, "status": 3}},
    }


# 请求地址
request_url = "https://api.xf-yun.com/v1/private/sc45f0684"

# 用于快速定位响应值

response_path_list = [
    "$..payload.output_text_result",
]
