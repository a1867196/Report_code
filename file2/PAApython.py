#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import csv
import subprocess
from PIL import Image

folder_path = r"D:\Adelaide\Trimester\2023 Trimester 3\MATHS 7097B - Data Science Res Proj Pt B"
csv_file_path = ".csv"
cut_w =
cut_h =
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Filename", "Row", "Col", "Z_Sum"])
    
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg"):
            image_path = os.path.join(folder_path, filename)
            image = Image.open(image_path)
            pixels = image.load()
            width, height = image.size
            z_sum = 0
            for x in range(width):
                for y in range(height):
                    color = pixels[x, y]
                    if color[0] >= 240 and color[0] <= 255 and color[1] <= 5 and color[2] <= 5:
                        z_sum += 1
            print(f"The total number of red points in {filename} is {z_sum}")
            
            subimage_width = width // cut_w
            subimage_height = height // cut_h
            for row in range(cut_h):
                for col in range(cut_w):
                    left = col * subimage_width
                    upper = row * subimage_height
                    right = left + subimage_width
                    lower = upper + subimage_height
                    subimage = image.crop((left, upper, right, lower))
                    subimage_pixels = subimage.load()
                    z_sum_sub = 0
                    for x in range(subimage_width):
                        for y in range(subimage_height):
                            color = subimage_pixels[x, y]
                            if color[0] >= 240 and color[0] <= 255 and color[1] <= 5 and color[2] <= 5:
                                z_sum_sub += 1
                    subimage_name = f"Subimage_{row}_{col}"
                    
                    csv_writer.writerow([filename, row, col, z_sum_sub])

subprocess.run(["start", csv_file_path], shell=True)

