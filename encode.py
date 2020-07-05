from PIL import Image
import math

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

if __name__ == '__main__':
    with open("三体全集.txt", encoding="utf-8") as f:
        all_text = f.read()
        
    im = encode(all_text)
    im.save("out.bmp")































#(index & 0xFF0000) >> 16