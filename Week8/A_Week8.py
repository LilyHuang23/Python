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
image_new.save("1.jpg")


#2nd picture
image_scat_g = Image.open("cat_small.jpg")
image_desert = Image.open("desert.jpg")
image_new2 = Image.new("RGB", image_scat_g.size)

width, height = image_scat_g.size

pixels_scat_g = image_scat_g.load()
pixels_desert = image_desert.load()
pixels_new = image_new2.load()

print(pixels_scat_g[50, 50])
print(pixels_scat_g[750, 50])
print(pixels_scat_g[50, 550])
print(pixels_scat_g[750, 550])

for y in range(height):
    for x in range(width):
        r, g, b = pixels_scat_g[x,y]
        if r<150 and g>100 and b<100:
            pixels_new[x,y] = pixels_desert[x,y]
        else:
            pixels_new[x,y] = pixels_scat_g[x,y]
image_new2.show()
image_new2.save("2.jpg")

#3
image_earth = Image.open("earth.jpg")
image_penguin_g = Image.open("penguin.jpg")
image_new3 = Image.new("RGB",image_penguin_g.size)

pixels_penguin_g = image_penguin_g.load()
pixels_earth = image_earth.load()
pixels_new3 = image_new3.load()

width, height = image_penguin_g.size
print(pixels_penguin_g[50, 50])
print(pixels_penguin_g[750, 50])
print(pixels_penguin_g[50, 550])
print(pixels_penguin_g[750, 550])


for y in range(height):
    for x in range(width):
        r,g,b = pixels_penguin_g[x,y]
        if r<100 and g>100 and b<100:
            #pixels_new3[x,y] = pixels_earth[x,y]
            r,g,b = pixels_earth[x,y]
            New_red = r + 100
            pixels_new3[x,y] = New_red,g,b
        else:
            pixels_new3[x,y] = pixels_penguin_g[x,y]
image_new3.show()
image_new3.save("3.jpg")
        

'''
r, g, b = pixels_original[100, 200]
print(r, g, b)
pixels_original[100,195] = (0, 0, 0)
pixels_original[100,196] = (0, 0, 0)
pixels_original[100,197] = (0, 0, 0)
pixels_original[100,198] = (0, 0, 0)
pixels_original[100,199] = (0, 0, 0)

image_original.save("beach_with_black_pixels.jpg")
'''