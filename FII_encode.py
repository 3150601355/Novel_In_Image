# -*- coding: utf-8 -*-
from PIL.Image import new
from math import ceil

def encode(data=bytes, change=int):
    '''
    + data: 文件的二进制数据
    + change: 文件二进制字节数字偏移的大小,可以是正整数或负整数,以此实现加密,输入0则不加密
    '''
    # 文件二进制数据的大小
    data_len = len(data)
    # 图片的宽
    w = ceil(data_len**0.5)
    # 创建一个新的图像
    im = new('L', (w, w))
    x, y = 0, 0
    for byte in data:
        # 将对应字节的值转为颜色填充到图像
        index = change + byte
        im.putpixel((x, y), index)
        if x == w -1:
            x = 0
            y += 1
        else:
            x += 1
    return im


def main(filename=str, change=int,saved_format='png'):
    '''
    + filename: 文件名,需添加后缀
    + change: 文件二进制字节数字偏移的大小,可以是正整数或负整数,以此实现加密,输入0则不加密
    '''
    with open(filename, 'rb') as fp:
        data = fp.read()
        out = encode(data, change)
        out.save(f'out.{saved_format}')


if __name__ == "__main__":
    filename = input('filename:')
    change = int(input('change:'))
    main(filename, change)
