import os

notes_dir = r"c:\Users\LENOVO\OneDrive\Desktop\Dynamic Skill\company profile\notes"
for f in sorted(os.listdir(notes_dir)):
    if f.endswith('.txt'):
        path = os.path.join(notes_dir, f)
        with open(path, 'r', encoding='utf-8-sig') as file:
            content = file.read().strip()
        print(f"{f}: {repr(content)}")
