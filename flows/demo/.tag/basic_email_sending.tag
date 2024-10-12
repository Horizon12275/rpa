// 设置电子邮件的相关信息
email_username = 'horizon52183'
email_password = '3e4r5t6y7uSED'
email_to = 'horizon52183@outlook.com'
email_subject = 'Test Email测试'
email_body = 'This is a test email sent using TagUI.测试'

// 打开 163
https://mail.163.com/

// 重置一下屏幕焦点
keyboard [enter]

// dom document.getElementsByTagName("iframe")[0].removeAttribute("name")
// dom document.getElementsByTagName("iframe")[0].setAttribute("name","login_iframe")

// // 登录
// frame login_iframe
// {
//     // 输入用户名
//     type //*[@class="u-input box"] as `email_username`

//     // 输入密码
//     type //*[@name="password"] as `email_password`

//     // 点击登录
//     click //*[@id="dologin"]
// }

// 登录邮箱
// 切换输入法（可能会不同）
keyboard [ctrl][space]
// keyboard horizon52183
keyboard [tab]
keyboard `email_password`
keyboard [enter]

// 点击写信
click //*[text()="写 信"]

// 输入收件人
type //*[@type="text" and @role="combobox"] as `email_to`

// 输入主题
type //div[@aria-label="邮件主题输入框，请输入邮件主题"]//*[@class="nui-ipt-input" and @type="text"] as `email_subject`

// 设置正文的iframe的name属性，以便于后续操作
dom document.getElementsByClassName("APP-editor-iframe")[0].setAttribute("name","email_body_iframe")

// 输入正文
frame email_body_iframe
{
    type //*[@class="nui-scroll"] as `email_body`
}

// 上传附件
upload .O0 as ./basic_excel.tag

// 点击发送
click //*[text()="发送"]