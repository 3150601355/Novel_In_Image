# -*- coding: utf-8 -*-
from PIL.Image import open as ImOpen

# 遇到大文件可以加上
# Image.MAX_IMAGE_PIXELS = 10000000000

def decode(im, change):
    '''
    + im: encode后的图像
    + change: 需要与encode时的change相同,以此进行解密,如无加密则输入0
    '''
    w, h = im.size
    lst = []
    for y in range(h):
        for x in range(w):
            index = im.getpixel((x, y))
            byte = index - change 
            if byte == ~change+1:
                break
            lst.append(byte)
    return bytes(lst)


def main(filename=str, change=int,saved_format='png'):
    '''
    + filename: 文件名,需添加后缀
    + change: 需要与encode时的change相同,以此进行解密,如无加密则输入0
    '''
    with open(filename, 'wb') as f:
        im = ImOpen(f'out.{saved_format}')
        byte = decode(im, change)
        f.write(byte)


if __name__ == "__main__":
    filename = input('filename:')
    change = int(input('change:'))
    main(filename, change)
