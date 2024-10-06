import rpa as r

# 好像能用
r.init(visual_automation = True)
r.dclick('outlook_icon.png')
r.click('new_mail.png')
r.type('message_box.png', 'Hi Gillian,[enter]This is ...')
r.click('send_button.png')
r.close()