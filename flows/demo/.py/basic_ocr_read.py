import rpa as r

# [RPA][ERROR] - cannot find b0.jpg 真牛，目前用不了
r.init(visual_automation = True, chrome_browser = False)
print(r.read('../.png/b0.jpg'))
r.close()