import os
from PIL import Image
import cv2
# 指定原始图片文件夹路径
folder_path = r"F:\xsy\0617shiebie\x"

# 指定目标文件夹路径
output_folder = r"F:\xsy\0617shiebie/"

# 获取文件夹内所有图片文件名
image_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg')or f.endswith('.png')]
def increase_resolution(img_path, scale_percent):
    img = cv2.imread(img_path)
    width = int(img.shape[1] * scale_percent )
    height = int(img.shape[0] * scale_percent )
    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(output_path, resized)

# 指定放大倍数
scale_percent = 2#将图片放大两倍

# 循环读取图片并将分辨率提高
for img_file in image_files:
    img_path = os.path.join(folder_path, img_file)
    output_path = os.path.join(output_folder, img_file)
    increase_resolution(img_path, scale_percent)