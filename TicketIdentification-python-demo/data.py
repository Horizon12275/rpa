APPId = "XXXXX"
APIKey = "XXXXX"
APISecret = "XXXXX"

# 请求数据
request_data = {
	"header":{
		"app_id":"123456",
		"status":3
	},
	"parameter":{
		"ocr":{
			"type":"air_itinerary",
			"level":1,
			"result":{
				"encoding":"utf8",
				"compress":"raw",
				"format":"json"
			}
		}
	},
	"payload":{
		"image":{
			"encoding":"jpg",
			"image":"./resource/input/img_1.png",
			"status":3
		}
	}
}

# 请求地址
request_url = "https://cn-huadong-1.xf-yun.com/v1/inv"

# 用于快速定位响应值

response_path_list = ['$..payload.result', ]