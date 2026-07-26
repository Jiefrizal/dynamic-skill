import os

css_path = r"c:\Users\LENOVO\OneDrive\Desktop\Dynamic Skill\company profile\static\images\inhouse\animation\styles.css"

with open(css_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

targets = ['.diagram-grid', '.skill-card', '.skills-column', '.hexagon', '.core-hexagon-wrapper', '.cards-stack']
print("Locating CSS rules for layout components:")
for idx, line in enumerate(lines, 1):
    for t in targets:
        if t in line and '{' in line:
            print(f"{idx}: {line.strip()}")
