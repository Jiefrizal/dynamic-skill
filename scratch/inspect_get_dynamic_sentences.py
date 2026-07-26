import os

app_path = r"c:\Users\LENOVO\OneDrive\Desktop\Dynamic Skill\company profile\app.py"

with open(app_path, 'r', encoding='utf-8') as f:
    content = f.read()

import re
matches = re.findall(r'def\s+get_dynamic_sentences[\s\S]*?(?=def\s+|\Z)', content)
for m in matches:
    print(m)
