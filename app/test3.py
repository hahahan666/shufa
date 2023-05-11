# 导入必要的模块
import numpy as np
import cv2
from matplotlib import pyplot as plt

# 加载原始图像
img = cv2.imread('test.jpg')

# 转换为灰度图像并进行阈值化处理
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# 使用find_contours()函数找到文字轮廓
contours, hierarchies = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# 遍历每个轮廓，并绘制边界框
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    if w * h > 70000: # 过滤掉过小的区域
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

# 显示结果图像
plt.imshow(img)
plt.show()