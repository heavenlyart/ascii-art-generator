def parse_bmp(filePath: str) -> list[list[tuple]]:
    """
    Takes in the file path of the bitmap image and parses the header and
    pixel data, storing the RGB channels of each pixel in an array and
    returns the pixel data as an array with all the pixel values.
    
    :param filePath: file path of the bmp image
    :type filePath: str
    :return: pixel data containing the RGB values of each pixel
    :rtype: list
    """ 
    pixel_data = []
    try:
        with open(filePath, 'rb') as bmp:
            # reading the header and checking if the file is a bmp image
            signature = bmp.read(2).decode('ascii')
            
            # checking for bitmap file signature in file provided
            if signature != 'BM':
                raise ValueError("The file is not a bitmap image.")
            
            # skipping useless values in header
            bmp.read(8)
            
            pixel_offset = int.from_bytes(bmp.read(4),'little')
            header_size = int.from_bytes(bmp.read(4),'little')
            width = int.from_bytes(bmp.read(4), 'little', signed=True)
            height = int.from_bytes(bmp.read(4), 'little', signed=True)
            
            # skipping useless values in DIB header
            bmp.read(2)
            
            color_depth = int.from_bytes(bmp.read(2), 'little')
            
            # seeking to where the pixel data starts
            bmp.seek(pixel_offset)
            
            # calculating total number of bytes necessary to store one
            # row of pixels and the padding in each row
            row_size = ((color_depth * width + 31) // 32) * 4
            padding = row_size - ((color_depth * width) // 8)
            
            for _ in range(abs(height)):
                row = []
                for _ in range(width):
                    if color_depth == 24:
                        blue = ord(bmp.read(1))
                        green = ord(bmp.read(1))
                        red = ord(bmp.read(1))
                        row.append((red, green, blue))
                    elif color_depth == 32:
                        blue = ord(bmp.read(1))
                        green = ord(bmp.read(1))
                        red = ord(bmp.read(1))
                        bmp.read(1) # skipping the alpha channel
                        row.append((red, green, blue))
                    else:
                        raise ValueError("Unsupported bit depth")
                bmp.read(padding)  #skip padding bytes
                pixel_data.append(row)
            
    except FileNotFoundError:
        print("Error : The file was not found at the specified location!")
        
    except TypeError:
        print("File selection cancelled or File is not of type bmp")
    
    pixel_data = pixel_data[::-1]
    return pixel_data


if __name__ == "__main__":
    print("""This file only has utility functions for the main program and does \
not have any functionallity on it's own.
Please run main.py to execute the program""")