# 导入必要的模块
import cv2
import numpy as np

# 加载原始图像
img = cv2.imread('test.jpg')

# 转换为灰度图像并进行阈值化处理
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# 使用形态学变换扩大文字区域
kernel = np.ones((5,5),np.uint8)
dilate = cv2.dilate(thresh,kernel,iterations = 4)

# 使用轮廓检测找到文字区域，并绘制边界框
contours, hierarchies = cv2.findContours(dilate,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
for c in contours:
    x,y,w,h = cv2.boundingRect(c)
    if w * h > 70000: # 过滤掉过小的区域
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

# 显示结果图像
cv2.imshow('img', img)
cv2.waitKey(0)