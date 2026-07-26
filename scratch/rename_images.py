import os

image_folder = r"c:\Users\LENOVO\OneDrive\Desktop\Dynamic Skill\company profile\static\images"

def clean_name(name):
    if '\u2502' in name:
        parts = name.split('\u2502')
        if len(parts) >= 3:
            org = parts[1].strip()
            rest = parts[2].strip()
            rest = rest.lstrip('-').strip()
            return f"{org} - {rest}"
        else:
            return name.replace('\u2502', '').strip()
    return name

def main():
    if not os.path.exists(image_folder):
        print("Image folder does not exist")
        return
        
    files = os.listdir(image_folder)
    renamed_count = 0
    
    for f in files:
        if '\u2502' in f:
            old_path = os.path.join(image_folder, f)
            new_f = clean_name(f)
            new_path = os.path.join(image_folder, new_f)
            
            # Formulate safe ASCII strings for printing
            safe_old = f.encode('ascii', errors='backslashreplace').decode('ascii')
            safe_new = new_f.encode('ascii', errors='backslashreplace').decode('ascii')
            
            try:
                os.rename(old_path, new_path)
                print(f"Renamed:\n  Old: {safe_old}\n  New: {safe_new}\n")
                renamed_count += 1
            except Exception as e:
                safe_err = str(e).encode('ascii', errors='backslashreplace').decode('ascii')
                print(f"Failed to rename {safe_old}: {safe_err}")
                
    print(f"Successfully renamed {renamed_count} files.")

if __name__ == '__main__':
    main()
