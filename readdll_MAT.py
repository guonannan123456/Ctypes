
# 通过动态库传递opencv MAT数据类型

# C++代码
# uchar* XLIB test(const char* json_path,const char* save_Path) {

#     Mat input_mat；

#     int height = input_mat.cols;
#     int width = input_mat.rows;
#     uchar* buffer = (uchar*)malloc(sizeof(uchar) * height * width*3);
#     memcpy(buffer, input_mat.data, height * width * 3);
#     return buffer;
# }
# XLIB void release(uchar* data) {
#     free(data);
# }


# python代码
import ctypes
from ctypes import *
import cv2
import numpy as np
jsonpath = "./json/2021.json"
savePath = "./figs"
pDll = CDLL("D:/Cpp.dll")
json_path = jsonpath.encode("utf-8")
save_Path = savePath.encode("utf-8")
pDll.test.restype = POINTER(c_ubyte)
img = pDll.test(json_path,save_Path)

dll_mat  =  np.array(np.fromiter(img, np.uint8,count=2917*3014*3))
dll_mat = dll_mat.reshape((2917,3014,3))
cv2.imshow('URL2Image',dll_mat)
cv2.waitKey()
pDll.release(img)
