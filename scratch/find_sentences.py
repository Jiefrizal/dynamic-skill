import os

app_path = r"c:\Users\LENOVO\OneDrive\Desktop\Dynamic Skill\company profile\app.py"

with open(app_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Let's find index route and see what variables it passes to home.html
import re
routes = re.findall(r'@app\.route\([\s\S]*?def\s+\w+[\s\S]*?return\s+render_template[\s\S]*?\)', content)
for r in routes:
    if "home.html" in r:
        print("Home route code:")
        print(r)
