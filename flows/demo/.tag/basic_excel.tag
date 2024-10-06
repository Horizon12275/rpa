
workbook = 'test'
sheet = 'Sheet1'
range = 'A:A'
block = 'A1'

// 写入 Excel 文件
[../.xlsx/`workbook`.xlsx]`sheet`!`block` = 123123123123123

// 读取 Excel 文件
data = [../.xlsx/`workbook`.xlsx]`sheet`!`range`
echo `data`