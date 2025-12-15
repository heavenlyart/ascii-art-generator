from pathlib import Path

def parseBMP(filePath: str) -> list:
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
            
    except FileNotFoundError:
        print("Error : The file was not found at the specified location!")
    
    return pixel_data
    
