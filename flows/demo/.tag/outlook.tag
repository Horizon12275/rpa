// 设置电子邮件的相关信息
email_username = 'horizon52183@outlook.com'
email_password = '0p9o8i7u6yFED'
email_to = '2309996590@qq.com'
email_subject = 'Test Email测试'
email_body = 'This is a test email sent using TagUI.测试'

// 打开 outlook
https://outlook.live.com/
wait 1s

// 点击登录
click //*[@class="wf-menu"]//*[text()="登录"]
wait 2s

click 登录 Outlook

// 输入用户名
type //input as `email_username`

// 点击下一个
click //*[text()="下一个"]

// 输入密码
type //input[@name="passwd"] as `email_password`

// 点击登录
click //*[text()="登录"]
click //*[text()="否"]

// 点击写信

// 输入收件人

// 输入主题

// 输入正文

// 上传附件

// 点击发送