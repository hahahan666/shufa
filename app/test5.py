import cv2
import numpy as np

# 读取图片并转换成灰度图
img = cv2.imread('test.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 对灰度图进行二值化处理，得到黑白图
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

# 对黑白图进行水平投影，得到每一行的像素和
h_projection = np.sum(binary, axis=1)

# 根据像素和判断每一行是否为空白，如果不为空白，则保存该行的上下边界
h_start = -1 # 行开始位置
h_end = -1 # 行结束位置
h_position = [] # 行位置列表

for i in range(len(h_projection)):
    if h_projection[i] > 0 and h_start == -1: # 非空白行且未开始记录位置时，记录开始位置为i
        h_start = i 
    elif h_projection[i] <= 0 and h_start != -1: # 空白行且已开始记录位置时，记录结束位置为i，并将开始结束位置加入列表中，并重置开始结束位置为-1
        h_end = i 
        h_position.append((h_start,h_end))
        h_start = -1 
        h_end = -1 

# 对每一行进行垂直投影，得到每一个字符的像素和，并根据像素和判断每一个字符是否为空白，
# 如果不为空白，则保存该字符的左右边界，并根据边界对图片进行切割，并保存切割后的图片

count = 0 # 计数器

for j in range(len(h_position)): # 遍历每一行
    
    start,end = h_position[j] # 获取该行的上下边界
    
    row_img = binary[start:end,:] # 截取该行对应的图片
    
    v_projection = np.sum(row_img,axis=0) # 对截取后的图片进行垂直投影
    
    v_start = -1 # 字符开始位置 
    v_end = -1 # 字符结束位置 
    
    for k in range(len(v_projection)): 
        
        if v_projection[k] > 0 and v_start == -1: # 非空白列且未开始记录位置时，记录开始位置为k
            
            v_start=k 
        
        elif v_projection[k] <= 0 and v_start != -1: # 空白列且已开始记录位置时，记录结束位置为k，并将截取出来的字符图片保存
            
            v_end=k 
            
            char_img=binary[start:end,v_start:v_end] 
            
            count+=1 
            
            cv2.imwrite('char_'+str(count)+'.jpg',char_img) 
            
            v_start=-1 
            v_end=-1 