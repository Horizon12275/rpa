import rpa as r

# 说实话没看懂这个图片是怎么使用的
r.init(visual_automation = True)
r.dclick('outlook_icon.png')
r.click('new_mail.png')
r.type('message_box.png', 'Hi Gillian,[enter]This is ...')
r.click('send_button.png')
r.close()