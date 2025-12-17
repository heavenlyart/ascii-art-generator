import random
from PIL import Image
import parser, image_processor, ascii
def create_random_image(pixel_data):
    # Create a new blank image with RGB mode
    height = len(pixel_data)
    width = len(pixel_data[0])

    image = Image.new("RGB", (width, height))
    pixels = image.load()

    for y in range(height):
        for x in range(width):
            r, g, b = pixel_data[y][x]
            pixels[x, y] = (r, g, b)

    return image

pixel_data = parser.parse_bmp('C:/pvs ka folder/coding project/python/ascii art generator/sample.bmp')
resized_image = image_processor.resize_img(pixel_data,2)
grayed_image = image_processor.convert_to_grayscale(resized_image)
ascii.pixel_to_ascii_gray(grayed_image) 
ascii.pixel_to_ascii_colored(resized_image,grayed_image)
# for i in ascii_image:
#     print(i)
# with open('image.txt','w' ) as file:
#     for i in ascii_image:
#         file.write(i)
#         file.write('\n')
        
# image = create_random_image(resized_image)
# image1 = create_random_image(grayed_image)
# image.save('random_image3.bmp')
# image1.save('random_image4.bmp')