import os

image_folder = r"c:\Users\LENOVO\OneDrive\Desktop\Dynamic Skill\company profile\static\images"

def main():
    if os.path.exists(image_folder):
        files = os.listdir(image_folder)
        print(f"Total files: {len(files)}")
        for idx, f in enumerate(files):
            ascii_name = f.encode('ascii', errors='backslashreplace').decode('ascii')
            print(f"{idx + 1}: {ascii_name}")
            
if __name__ == '__main__':
    main()
