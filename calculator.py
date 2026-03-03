import fsspec
import numpy as np
import cv2
import pandas as pd
import os

def get_gray_values(image_path):
    if contains_chinese(image_path):
        image = cv2.imdecode(np.fromfile(image_path, dtype = np.uint8), 2 | 0)
    else:
        image = cv2.imread(image_path, cv2.IMREAD_ANYDEPTH | cv2.IMREAD_GRAYSCALE)

    if image is None:
        raise FileNotFoundError(f"无法读取图像文件")

    gray_values = np.array(image)   
    return gray_values

def contains_chinese(text):
    for char in text:
        if '\u4e00' <= char <= '\u9fff':
            return True
    return False

def calculate_intensity(gray_values, threshold):
    filtered_values = np.where(gray_values > threshold, gray_values, 0)
    max_intensity = np.max(filtered_values)
    total_intensity = np.sum(filtered_values)
    average_intensity = total_intensity / (filtered_values.shape[0] * filtered_values.shape[1])
    return [max_intensity, total_intensity, average_intensity]

def process_images(file_address, threshold):
    data = []
    cnt = 0
    jpg_files_found = False

    for filename in sorted(os.listdir(file_address)):
        if filename.endswith(".jpg"):
            jpg_files_found = True
            jpg_name = filename.split('.jpg')[0]
            gray_values = get_gray_values(os.path.join(file_address, filename))
            intensity_data = calculate_intensity(gray_values, threshold)
            data.append([jpg_name] + intensity_data)
            cnt += 1

    if not jpg_files_found:
        raise FileNotFoundError(f"文件夹中没有找到任何 jpg 文件")
    
    df = pd.DataFrame(data, columns=["图像名称", "最大值", "总光强", "平均光强"])
    return df

def save_data(df, output_path):
    df.to_excel(output_path, index=False)