## TagUI

### 配置

1. 下载地址：https://github.com/aisingapore/TagUI/releases

2. 添加 D:\tagui\src 到环境变量 PATH

3. 更改 D:\tagui\src\tagui.cmd 中浏览器路径如下：

```cmd
# Before
set chrome_command=C:\Program Files (x86)\Google\Chrome\Application\chrome.exe
# After
set chrome_command=C:\Program Files\Google\Chrome\Application\chrome.exe
```

4. 配置 cmd 为 UTF-8 编码： win10 : https://blog.csdn.net/lyyybz/article/details/120782669 win11 : https://blog.csdn.net/jymd2508/article/details/135334716

```cmd
# 查看当前编码，应该是 936，即 GBK，输出为 65001时，即 UTF-8
chcp
```

5. cd D:\tagui\flows\samples

6. 运行示例、其中有些定位不出元素、所以会报错，跑了一遍其中貌似只有 3，5 是正常的、而且有些网站还会跳人机验证。

```cmd
tagui .\1_google.tag
tagui .\2_github.tag
tagui .\3_conditions.tag
tagui .\4_loops.tag
tagui .\5_repositories.tag
tagui .\6_datatables.tag
tagui .\7_newtab.tag
tagui .\8_chineseflow.tag
tagui .\9_lazada.tag
```
