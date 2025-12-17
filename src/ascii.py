import math   


def color_print(text: str, r: int, g: int, b: int) -> None:
    """
    Prints whatever text is given in colored in rgb using ansi escape 
    codes
    Works only if your terminal supports truecolor
    
    :param text: the text to be printed in color
    :type text: str
    :param r: red value 
    :type r: int
    :param g: green value
    :type g: int
    :param b: blue value
    :type b: int
    """
    
    color_code = f"\033[38;2;{r};{g};{b}m"
    reset_code = "\033[0m"
    print(f"{color_code}{text}{reset_code}",sep="", end="")
    
    
def pixel_to_ascii_gray(image: list[list[tuple]]) -> None:
    """
    Takes in an image object and prints out the ascii equivalent in
    grayscale.
    NOTE : This function was only for testing and is not currently being
    used in the program
    
    :param image: image object
    :type image: list[list[tuple]]
    """
    
    # initialising the set of characters that will make up the image
    characters =  "     .-=+*x#$&X@"
    characters_len = len(characters)
    
    # logic to determine luminosity of each pixel
    interval = characters_len/256
    
    for row in image:
        ascii_row = ""
        for pixel in row:
            print(characters[math.floor(pixel[0] * interval)],sep="",end="")
        print("\n",end="",sep="")


def pixel_to_ascii_colored(color_image: list[list[tuple]], 
                           gray_image:  list[list[tuple]]) -> None:
    """
    Takes in an image object and prints out the ascii equivalent in
    colored.
    
    :param color_image: colored image object
    :type color_image: list[list[tuple]]
    :param gray_image: grayscale image object
    :type gray_image: list[list[tuple]]
    """
    
    height = len(gray_image)
    width = len(gray_image[0])
    
    # initialising the set of characters that will make up the image
    characters = "    .-=+*x#$&X@"
    characters_len = len(characters)
    
    # logic to determine luminosity of each pixel
    interval = characters_len/256
    
    # iterating over each pixel and printing its ascii equivalent 
    for y in range(height):
        for x in range(width):
            r = color_image[y][x][0]
            g = color_image[y][x][1]
            b = color_image[y][x][2]
            
            color_print(characters[math.floor(gray_image[y][x][0] * interval)],
                        r,g,b)
        print("\n",end="")
        
if __name__ == "__main__":
    print("""This file only has utility functions for the main program and does \
not have any functionallity on it's own.
Please run main.py to execute the program""")