import os

js_path = r"c:\Users\LENOVO\OneDrive\Desktop\Dynamic Skill\company profile\static\images\inhouse\script.js"

if os.path.exists(js_path):
    with open(js_path, 'rb') as f:
        content_bytes = f.read(200)
    print("First 200 bytes:", repr(content_bytes))
    
    with open(js_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    print("File length:", len(content))
    print("Is 'canvas' in content?", "canvas" in content.lower())
    print("Is 'particle' in content?", "particle" in content.lower())
    print("Is 'laser' in content?", "laser" in content.lower())
    print("Is 'bgCanvas' in content?", "bgcanvas" in content.lower())
else:
    print("JS file does not exist")
