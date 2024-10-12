## 运行环境
python3.8
## 项目目录介绍
### requirements.txt
项目依赖包管理文件<br>
首次下载此项目后执行`pip3 install -r requirements.txt`即下载安装依赖包

### data.py
根据接口文档自动生成的相关配置（请根据接口文档配置所需的请求参数）
- 请求协议
- 请求地址
- 响应数据段，便于程序处理接口响应
- APPId、APIKey、APISecret信息

### main.py
程序的执行入口

### resource目录
此目录提供平台内置的请求文件以及后续保存程序执行响应文件

### sample目录
程序核心执行逻辑步骤

#### exception.py
自定义异常

#### ne_utils.py
工具文件 
- 读取问题获取文件内容
- 清空目录
- 生成鉴权的url
- 解析url获取对应的host、path、schema

#### aipaas_client.py
核心程序执行
- 数据准备 prepare_req_data
- 执行 execute
- 处理响应数据 deal_response