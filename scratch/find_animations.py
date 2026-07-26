import os
import re

js_path = r"c:\Users\LENOVO\OneDrive\Desktop\Dynamic Skill\company profile\static\images\inhouse\script.js"

with open(js_path, 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

print("Searching for canvas/particle/draw/laser function definitions:")
for idx, line in enumerate(lines, 1):
    # Match function definitions or class/variable definitions related to animation
    if 'function' in line or 'const ' in line or 'class ' in line or 'init' in line or 'draw' in line:
        if any(kw in line.lower() for kw in ['canvas', 'particle', 'draw', 'laser', 'bg', 'render', 'animate']):
            print(f"{idx}: {line.strip()}")
