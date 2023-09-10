#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from PIL import Image
image_path1 = r"D:\Adelaide\Trimester\2023 Trimester 3\MATHS 7097B - Data Science Res Proj Pt B\col10row8.jpg"
image_path2 = r"D:\Adelaide\Trimester\2023 Trimester 3\MATHS 7097B - Data Science Res Proj Pt B\col10row8.jpg"
image_path3 = r"D:\Adelaide\Trimester\2023 Trimester 3\MATHS 7097B - Data Science Res Proj Pt B\col10row8.jpg"
image_path4 = r"D:\Adelaide\Trimester\2023 Trimester 3\MATHS 7097B - Data Science Res Proj Pt B\col5row2.jpg"
image_path5 = r"D:\Adelaide\Trimester\2023 Trimester 3\MATHS 7097B - Data Science Res Proj Pt B\col5row2.jpg"
image_path6 = r"D:\Adelaide\Trimester\2023 Trimester 3\MATHS 7097B - Data Science Res Proj Pt B\col5row2.jpg"
image_path = [image_path1,image_path2,image_path3,image_path4,image_path5,image_path6]
for i in image_path:
    image = Image.open(i)
    pixels = image.load()
    width, height = image.size
    print(width, height)

