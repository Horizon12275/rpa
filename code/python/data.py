class APP:
    def __init__(self, APPId: str, APIKey: str, APISecret: str):
        self.APPId = APPId
        self.APIKey = APIKey
        self.APISecret = APISecret


# 创建 APP 实例并存储在列表中
APP_list = [
    APP(
        APPId="2aa011b8",
        APIKey="8bf74a4816a840f556b26dfd879461a3",
        APISecret="OGZkOTdiODJjMmZhZjE2MzBjOWU0MDA5",
    ),
    APP(
        APPId="49905e86",
        APIKey="b8602a5b887dde6d8d7c41204e149187",
        APISecret="NTRjMTkwZjYwNjUzYmE4ODM2ODNlNWIw",
    ),
    APP(
        APPId="a3c73bcc",
        APIKey="8f5eebefc0a97e5b2bffce05563d3eb1",
        APISecret="YjAyZGRlN2I5YTliNjdhMmE2ZWExNjI5",
    ),
    APP(
        APPId="b576e26a",
        APIKey="163c61dcad53ec2d0853428cd171d4b0",
        APISecret="NDYwZGU4ZTQzOTk1MTIzODk3NWVlYjcx",
    )
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
