'''
file: Week 7 assignment
'''
from PIL import Image
print("correctly")

image_original = Image.open("beach.jpg")
image_green = Image.open("penguin.jpg")
image_new = Image.new("RGB", image_green.size)

width, height = image_original.size


pixels_original = image_original.load()
pixels_green = image_green.load()
pixels_new = image_new.load()

print(pixels_green[50, 50])
print(pixels_green[750, 50])
print(pixels_green[50, 550])
print(pixels_green[750, 550])

for y in range(height):
    for x in range(width):
        r, g, b = pixels_green[x,y]
        if r<150 and g>100 and b<100:
            pixels_new[x,y] = pixels_original[x,y]
        else:
            pixels_new[x,y] = pixels_green[x,y]
image_new.show()








r, g, b = pixels_original[100, 200]
print(r, g, b)
pixels_original[100,195] = (0, 0, 0)
pixels_original[100,196] = (0, 0, 0)
pixels_original[100,197] = (0, 0, 0)
pixels_original[100,198] = (0, 0, 0)
pixels_original[100,199] = (0, 0, 0)

image_original.save("beach_with_black_pixels.jpg")
