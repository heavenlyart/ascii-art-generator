def resize_img(image: list[list[tuple]], scale: int  = 4) ->list[list[tuple]]:
    """
    Downsamples the image while making sure the height to width ratio is
    2:1 to account for the font used in default windows terminal.
    A box filter is used to average over the pixel values over a given 
    region and that value for the new pixel
    
    :param image: image object containing pixel data
    :type image: list[list[tuple]]
    :param scale: scaling factor used in downsampling
    :type scale: int
    :return: downsampled image object
    :rtype: list[list[tuple]]
    """
    
    # making sure that height is twice that of width when downsampled
    w_scale = scale
    h_scale = scale * 2
    
    orig_h = len(image)
    orig_w = len(image[0]) if orig_h > 0 else 0
    
    # calculate new dimensions of the image using floor division
    new_h = orig_h // h_scale
    new_w = orig_w // w_scale
    
    # initialize an image object
    downsampled = [[(0, 0, 0) for _ in range(new_w)] for _ in range(new_h)]
    
    # iterating over every pixel of the new image
    for y in range(new_h):
        for x in range(new_w):
            
            # initialising variables to use for the average
            r_sum, g_sum, b_sum = 0, 0, 0
            count = 0
            
            # creating an imaginary box inside the image
            y_start = y * h_scale
            y_end = (y + 1) * h_scale
            x_start = x * w_scale
            x_end = (x + 1) * w_scale
            
            # iterating over the pixels inside the box
            for i in range(y_start, y_end):
                for j in range(x_start, x_end):
                    r, g, b = image[i][j]
                    
                    #adding all the channel values together to average
                    r_sum += r
                    g_sum += g
                    b_sum += b
                    count += 1
            
            # calculating average channel value
            downsampled[y][x] = (r_sum // count, g_sum // count, b_sum // count)
            
    return downsampled

def convert_to_grayscale(image: list[list[tuple]]) -> list[list[tuple]]:
    """
    Converts the given image to a grayed out image using the luminosity
    method.
    
    :param image: pixel data of the image
    :type image: list[list[tuple]]
    :return: grayed out image pixel data
    :rtype: list[list[tuple]]
    """
    
    grayed_image = []
    
    # iterating over all the pixels inside the image
    for row in image:
        new_row = []
        for pixel in row:
            r, g, b = pixel
            
            # converting each pixel to grayscale using luminosity method
            gray_pixel_value = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
            gray_pixel = (gray_pixel_value, gray_pixel_value,
                          gray_pixel_value)
            
            new_row.append(gray_pixel)
        grayed_image.append(new_row)
    
    return grayed_image

if __name__ == "__main__":
    print("""This file only has utility functions for the main program and does \
not have any functionallity on it's own.
Please run main.py to execute the program""")