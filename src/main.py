from parser import parse_bmp
from image_processor import resize_img, convert_to_grayscale
from ascii import pixel_to_ascii_colored
from pathlib import Path
import tkinter as tk
from tkinter import filedialog

def select_file() -> str | None:
    """
    Creates a Tkinter window to select a bitmap image and then return
    it's path for later use
    
    :return: returns the path of the image selected as str or None if 
    no file is selected
    :rtype: str | None
    """
    
    # hide the main Tkinter window
    root = tk.Tk()
    root.withdraw() 
    
    filetypes = (
        ('bmp files', '*.bmp'),
        ('All files', '*.*')
    )

    # open the file dialog and get the selected file path as a string
    file_path_str = filedialog.askopenfilename(
        title='Open a file',
        initialdir=Path.home(), # start in the user's home directory
        filetypes=filetypes
    )

    if file_path_str:
        # Convert the string to a Path object
        user_path = Path(file_path_str)
        print(f"Selected file: {user_path}")
        return user_path
        
    else:
        return None

file = select_file()

try:
    # parsing the bitmap image
    parsed_img = parse_bmp(file)
    
    if parsed_img != []:
        
        # downsampling the image
        # NOTE : ADD A POSITIVE INTEGER VALUE AFTER parsed_img TO CHANGE THE 
        # SCALE OF THE IMAGE INCASE IT'S TOO BIG (DEFAULT IS 4)
        # BIG NUMBER -> SMALLER IMAGE
        # SMALL NUMBER -> BIGGER IMAGE
        downsampled_img = resize_img(parsed_img)

        # turning the image to grayscale
        grayed_img = convert_to_grayscale(downsampled_img)

        # converting the image to ascii and printing it to the terminal
        # takes in two images to account for the coloring
        pixel_to_ascii_colored(downsampled_img,grayed_img)
    
    else:
        raise Exception("Please select a valid BMP image")
    
except:
    raise Exception("Please select a valid BMP image")