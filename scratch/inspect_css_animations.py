import os

css_path = r"c:\Users\LENOVO\OneDrive\Desktop\Dynamic Skill\company profile\static\images\inhouse\styles.css"

with open(css_path, 'r', encoding='utf-8') as f:
    content = f.read()

import re
keyframes = re.findall(r'@keyframes\s+\w+', content)
print("CSS Keyframes found:")
for k in keyframes:
    print("  -", k)
