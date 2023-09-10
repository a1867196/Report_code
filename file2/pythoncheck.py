#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from PIL import Image
image_path1 = r"D:\Adelaide\Trimester\2023 Trimester 3\MATHS 7097B - Data Science Res Proj Pt B\.jpg"
image_path2 = r"D:\Adelaide\Trimester\2023 Trimester 3\MATHS 7097B - Data Science Res Proj Pt B\.jpg"
image_path = [image_path1,image_path2]
for i in image_path:
    image = Image.open(i)
    pixels = image.load()
    width, height = image.size
    z_sum = 0
    for x in range(width):
        for y in range(height):
            color = pixels[x, y]
            if color[0] >= 250 and color[0] <= 255 and color[1] <= 5 and color[2] <= 5:
                z_sum =  z_sum + 1 
    print(".jpg z values:", z_sum)

