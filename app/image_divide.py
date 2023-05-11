import cv2
import numpy as np

# 读取图片
img = cv2.imread('test.jpg')
# 转为灰度图
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# 二值化
ret,binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)

# 水平投影
h,w = binary.shape
h_projection = np.zeros(binary.shape,dtype=np.uint8)
# 图像高度
h_sum = np.sum(binary,axis=1)
for i in range(h):
    if h_sum[i] > 0:
        h_projection[i,:] = 255

# 垂直投影
v_projection = np.zeros(binary.shape,dtype=np.uint8)
w_sum = np.sum(binary,axis=0)
for i in range(w):
    if w_sum[i] > 0:
        v_projection[:,i] = 255

# 根据水平投影获取每一行的位置
position_h = []
start_h = 0
end_h = 0
for i in range(h-1):
    if h_sum[i] == 0 and h_sum[i+1] > 0:
        start_h = i+1 # 行开始位置
    elif h_sum[i] > 0 and h_sum[i+1] == 0:
        end_h = i # 行结束位置
        position_h.append([start_h,end_h]) # 添加到列表中

# 根据垂直投影获取每个字符的位置，并分割出每个字符
index = 0 # 字符索引号，用于保存图片时命名
for row in position_h: # 遍历每一行的位置信息
    start_row,end_row = row # 获取行开始和结束位置 
    position_w = [] # 存储每个字符的位置信息（列）
    start_w = 0 
    end_w = 0 
    for j in range(w-1): 
        if w_sum[j] == 0 and w_sum[j+1] > 0: 
            start_w= j+1 # 字符开始位置（列）
        elif w_sum[j]>0 and w_sum[j+1]==0: 
            end_w=j # 字符结束位置（列）
            position_w.append([start_w,end_w]) # 添加到列表中
    
    for col in position_w: # 遍历每个字符的位置信息（列）
        start_col,end_col=col # 获取字符开始和结束位置（列）
        char_img=binary[start_row:end_row,start_col:end_col] # 分割出字符图片
        
        index +=1 
        cv2.imwrite('char_'+str(index)+'.jpg',char_img) #保存字符图片