# Novel_In_Image

## 1.功能介绍

这是一个可以让文字和图片互相转换的便利工具。它可以用来隐藏小说之类的文本内容。

原理及视频教程：
https://www.bilibili.com/video/BV1Ai4y1V7rg/

## 2.用法

### 文字转图片：

```python
python nii.py -e xxx.txt
```

其中`xxx.txt`是要转换的文本路径。

### 图片转文字

```python
python nii.py -d xxx.bmp
```

其中`xxx.bmp`是要转换的图片路径。

## 3.注意事项

在开始使用之前，请确保您的设备已经安装了Python 3.6或更新版本，和`pillow`库。如果没有安装`pillow`，我给大家提供了一个方便的方式来安装，只需

```python
python nii.py -i
```

等待安装完成即可。
