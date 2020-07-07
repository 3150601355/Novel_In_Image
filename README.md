# Novel_In_Image

## 功能介绍

NII是一个在文字和图片之间互相转换的便利工具。可以有效地隐藏文本内容或者在设备之间方便地传输。与彩色二维码作用类似。

## 用法

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

## 使用前

在开始使用之前，请确保您的设备已经安装了Python 3.6或更新版本，和`pillow`库。如果没有安装`pillow`，我们提供了一个方便的方式来安装，只需

```python
python nii.py -i
```

等待安装完成即可。
