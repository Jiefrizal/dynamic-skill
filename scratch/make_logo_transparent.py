import os
from PIL import Image

logo_path = r"c:\Users\LENOVO\OneDrive\Desktop\Dynamic Skill\company profile\static\images\logo\logo.png"

if os.path.exists(logo_path):
    try:
        # Load and convert to RGBA
        img = Image.open(logo_path).convert('RGBA')
        
        # Save backup first (using standard .png extension to avoid Pillow errors)
        backup_path = logo_path.replace("logo.png", "logo_backup.png")
        if not os.path.exists(backup_path):
            img.save(backup_path)
            print(f"Original logo backed up to: {backup_path}")
            
        # Get pixels and modify alpha
        # We can use load() which is faster and doesn't trigger deprecation warnings
        pixels = img.load()
        width, height = img.size
        
        for y in range(height):
            for x in range(width):
                r, g, b, a = pixels[x, y]
                # If pixel is white or near-white (background), make it transparent
                if r > 240 and g > 240 and b > 240:
                    pixels[x, y] = (255, 255, 255, 0)
                    
        img.save(logo_path, "PNG")
        print("Successfully made logo background transparent and updated logo.png!")
    except Exception as e:
        print(f"Error making logo transparent: {e}")
else:
    print("Logo file does not exist")
