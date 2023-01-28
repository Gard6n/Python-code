from PIL import Image
print("Choose your animal: ")
animal = input()
cake = Image.open(animal + ".jpg")
width, height = cake.size
pix = cake.load()
for x in range(height):
    for y in range(width):
        r, g, b = pix[y, x]
        if r == 44 or r == 43 or r == 41 or r == 67 or r == 66:
            if g == 207 or g == 209 or g == 229:
                if b == 64 or b == 57 or b == 62 or b == 60 or b == 24:
                    pix[y, x] = (255,255,255)
print("Choose your background:")
bg = input()
background = Image.open(bg + ".jpg")
pix_back = background.load()
for x in range(height):
    for y in range(width):
        r, g, b = pix[y, x]
        if r == 255:
            if g == 255:
                if b == 255:
                    r, g, b = pix_back[y, x]
                    pix[y, x] = ( r, g, b)
cake.show()
print ("Please name your image without spaces: ")
name = input()
cake.save(name + ".jpg")