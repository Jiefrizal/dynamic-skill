import os
from PIL import Image

logo_path = r"c:\Users\LENOVO\OneDrive\Desktop\Dynamic Skill\company profile\static\images\logo\logo.png"

if os.path.exists(logo_path):
    try:
        img = Image.open(logo_path)
        print(f"Format: {img.format}, Size: {img.size}, Mode: {img.mode}")
        
        # Check transparency
        if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
            # Check if there is actual transparency
            alpha = img.convert('RGBA').split()[-1]
            bbox = alpha.getbbox()
            if bbox:
                # check if there are non-transparent pixels in corners
                pixels = list(alpha.getdata())
                transparent_count = pixels.count(0)
                total_pixels = len(pixels)
                print(f"Transparency detected: {transparent_count} transparent pixels out of {total_pixels} ({transparent_count/total_pixels*100:.2f}%)")
            else:
                print("Image is fully transparent")
        else:
            print("Image does not support transparency (solid background)")
    except Exception as e:
        print(f"Error opening image: {e}")
else:
    print("Logo file does not exist")
