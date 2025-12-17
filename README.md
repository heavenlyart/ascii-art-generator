# ASCII Art Generator

A simple **ASCII Art Generator written entirely in Python**, designed to convert bitmap images into colorful ASCII representations directly in your terminal — no external libraries required.

---

## Overview

This project takes a bitmap image as input, processes its raw pixel data, and transforms it into ASCII art while preserving brightness and color information. The entire pipeline is built using **only Python’s standard library**, making it lightweight, portable, and easy to run anywhere Python is available.

---

## Features

- **Pure Python** — uses only the Python standard library  
- *Bitmap image parsing** to extract pixel-level data  
- **Image downscaling** using a box filter to reduce resolution  
- **Grayscale conversion** for accurate luminosity mapping  
- **Colored ASCII output** printed directly in the terminal  

---

## How It Works

1. **Parsing the bitmap image**  
   The program reads the bitmap image and extracts RGB pixel data.

2. **Downscaling image using Box Filter**  
   To reduce resolution, a box filter is applied over pixel regions, averaging values to preserve image structure.

3. **Converting image to grayscale**  
   Each pixel is converted to grayscale to accurately estimate luminosity.

4. **ASCII Mapping**  
   Pixel brightness values are mapped to ASCII characters based on intensity.

5. **Terminal Rendering**  
   The ASCII art is printed to the terminal using color codes to retain the original image’s feel.

---

## Requirements

- Ensure you have **Python 3.10** installed
- No external libraries or dependencies needed

---

## Usage

1. Clone the repository:
   ```
   gh repo clone pvsssss/ascii-art-generator
   cd ascii-art-generator
2. Run the program:
```
python main.py
```

3. Select a bitmap image when prompted
   The program will handle the rest automatically.

---

## Configuration

If the output image appears too large, adjust the scaling factor:
- Open `main.py`
- Locate the `SCALE` variable and increase it's value

---

# Notes

- Works only with bitmap images
- Terminal must support truecolor for colored output

---

## Acknowledgments

This project was inspired and guided by learning resources from:

- [Xander Gouws' video on making an ascii art generator in C](https://www.youtube.com/watch?v=t8aSqlC_Duo)
- [Kay Lack's video on BMP images](https://www.youtube.com/watch?v=13E0il2zxBA)
- [Wikipedia article on ansi escape codes t](https://en.wikipedia.org/wiki/ANSI_escape_code)

---

# Contact

Feel free to reach out or connect with me:
- LinkedIn: [@PratakhveerSingh](https://www.linkedin.com/in/pratakhveersingh)
- Instagram: [@singh_pratakhveer](https://www.instagram.com/singh_pratakhveer)

# Screenshots
<img src="./samples/sample1 in ascii.jpeg" alt="Project Screenshot" >
<img src="./samples/sample2 in ascii.jpeg" alt="Project Screenshot" >
<img src="./samples/sample3 in ascii.jpeg" alt="Project Screenshot" >
