from Crypto.Cipher import AES
from PIL import Image
import math
import sys
import os


iv = b'1234567812345678' # iv偏移量，bytes类型

def help():
    print("提供 Novel_In_Image 命令的帮助信息。")
    print()
    print("enc [fileName]")
    print()
    print("\t fileName - 写出该文件对应的图片。")
def encode(text):
    str_len = len(text)
    width = math.ceil(str_len**0.5)
    im = Image.new("RGB", (width, width), 0x0)

    x, y = 0, 0
    for i in text:
        index = ord(i)
        rgb = ( 0,  (index & 0xFF00) >> 8,  index & 0xFF)
        im.putpixel( (x, y),  rgb )
        if x == width - 1:
            x = 0
            y += 1
        else:
            x += 1
    return im
def AES(text,key)
    aes = AES.new(key,AES.MODE_ECB)
    en_text = aes.encrypt(text) #AES加密
    return en_text.decode("utf-8")
def main(filename: str):
    t = bytes(input("请输入Key"), encoding='utf-8')
    with open(filename, encoding="utf-8") as f:
        all_text = AES(f.read(),t)
    im = encode(all_text)
    im.save("{}_layout.bmp".format('.'.join(filename.split('.')[:-1])))
    
if __name__ == '__main__':
    os.system("color 3e") #背景蓝色 字体黄色(字体挺像我(划掉
    if sys.argv[1] == 0:
        help()
    else:
        main(str(sys.argv[1]))

#(index & 0xFF0000) >> 16
