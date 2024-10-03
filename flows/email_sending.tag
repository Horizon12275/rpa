// 设置电子邮件的相关信息
email_to = 'horizon52183@outlook.com'
email_subject = 'Test Email测试'
email_body = 'This is a test email sent using TagUI.测试'

// 打开163
https://mail.163.com/

// 登录邮箱
keyboard [enter]
// 切换输入法（可能会不同）
keyboard [ctrl][space]
keyboard horizon52183
keyboard [tab]
keyboard 3e4r5t6y7uSED
keyboard [enter]

// 点击写信
click //*[text()="写 信"]

// 输入收件人
type //*[@type="text" and @role="combobox"] as `email_to`

// 输入主题
type //div[@aria-label="邮件主题输入框，请输入邮件主题"]//*[@class="nui-ipt-input" and @type="text"] as `email_subject`

// 点击发送
click //*[text()="发送"]