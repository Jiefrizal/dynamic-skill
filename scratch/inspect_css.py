import os
import re

css_path = r"c:\Users\LENOVO\OneDrive\Desktop\Dynamic Skill\company profile\static\css\style.css"

if os.path.exists(css_path):
    with open(css_path, 'rb') as f:
        content_bytes = f.read()
    print("First 200 bytes:", repr(content_bytes[:200]))
    
    with open(css_path, 'r', encoding='utf-8') as f:
        content = f.read()
    print("First 200 chars:", repr(content[:200]))
else:
    print("CSS file does not exist")
