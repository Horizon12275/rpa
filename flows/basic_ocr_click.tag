https://www.baidu.com/

// 只支持英文
// click hao123 using OCR

// 下面的代码没法用
// vision begin
// import org.sikuli.script.TextRecognizer as TR
// Settings.OcrReadText = True
// Settings.OcrLanguage = "chi_sim"
// TR.reset()
// click 登录 using OCR
// vision finish

// visit IRAS website (for managing taxes in Singapore)
https://www.iras.gov.sg/irashome/default.aspx

// click IRAS

// bring Chrome web browser to foreground to be in focus,
// for subsequent steps to click visually on UI elements
// click chrome_icon.png

// increase timeout from default 10 seconds to 300 seconds
// to let user sign in, including using 2FA authentication
timeout 300

// log in to personal income tax using visual automation,
// instead of specifying XPath or other web identifiers
// that natively interact with web browser's backend
click login_menu.png
click mytax_option.png
click personal_button.png