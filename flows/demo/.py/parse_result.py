import json

# 初始化result
result = None

# 从../dataset_test/b0.json文件中读取json格式的数据
with open('../dataset_test/b0.json', 'r') as f:
    result = json.load(f)
    # print(result)

# 从result中解析有用的发票信息，值对应的名字都在object_list[n].region_list[n].text_block_list[n].key里面
# 值对应的内容都在object_list[n].region_list[n].text_block_list[n].value里面
# 遍历object_list，解析并保存有用的信息对象到invoice字典中
invoice = {}

for object in result['object_list']:
    # 遍历region_list
    for region in object['region_list']:
        # 遍历text_block_list
        for text_block in region['text_block_list']:
            # 解析有用的信息
            key = text_block['key']
            value = text_block['value']
            # 保存到invoice字典中
            invoice[key] = value

# 打印invoice字典，每个键值对间隔一行
for key, value in invoice.items():
    print(f"{key}: {value}")
    print()