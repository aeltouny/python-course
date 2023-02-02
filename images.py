from PIL import Image,ImageFilter

img = Image.open('./pokedex/pikachu.jpg')

filtered_img = img.filter(ImageFilter.BLUR)

filtered_img.save('bulired.png' ,'png')


sharpen_img = img.filter(ImageFilter.SHARPEN)

sharpen_img.save('sharpen.png', 'png')

gray_img = img.convert('L')

gray_img.save('gray.png' , 'png')

print(img)

print('Fromat : ' , img.format)

print('Image Size : ' , img.size)


print('Color channel : ' , img.mode)