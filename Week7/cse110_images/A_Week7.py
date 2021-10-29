'''
file: Week 7 assignment
'''
from PIL import Image
print("correctly")

image_original = Image.open("beach.jpg")
width = 300
height = 300
width, height = image_original.size


pixels_original = image_original.load()
r, g, b =pixels_original[100, 200]
print(r, g, b)
pixels_original[100,195] = (0, 0, 0)
pixels_original[100,196] = (0, 0, 0)
pixels_original[100,197] = (0, 0, 0)
pixels_original[100,198] = (0, 0, 0)
pixels_original[100,199] = (0, 0, 0)

image_original.save("beach_with_black_pixels.jpg")
