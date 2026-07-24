import os
import re

css_path = r"c:\Users\LENOVO\OneDrive\Desktop\Dynamic Skill\company profile\static\css\style.css"

if os.path.exists(css_path):
    with open(css_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    lines = content.split('\n')
    print(f"Total lines: {len(lines)}")
    
    # Print lines matching search terms
    search_terms = ['company', 'navbar', 'brand', 'logo', 'border', 'background', 'box']
    for i, line in enumerate(lines):
        for term in search_terms:
            if term in line.lower():
                print(f"Line {i+1}: {line.strip()}")
                break
else:
    print("CSS file does not exist")
