import pytesseract
from PIL import Image
 
def demo():
    # 打开要识别的图片
    image = Image.open('../.png/b0.jpg')
    # 使用pytesseract调用image_to_string方法进行识别，传入要识别的图片，lang='chi_sim'是设置为中文识别，lang='eng'是英文识别
    text = pytesseract.image_to_string(image, lang='chi_sim')
 
    # 输出所识别的文字
    print(text)
 
if __name__ == '__main__':
    demo()
 