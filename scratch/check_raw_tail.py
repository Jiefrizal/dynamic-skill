import os

css_path = r"c:\Users\LENOVO\OneDrive\Desktop\Dynamic Skill\company profile\static\css\style.css"

if os.path.exists(css_path):
    with open(css_path, 'rb') as f:
        f.seek(-1000, 2)
        raw = f.read()
    print(f"Tail raw bytes: {raw[:300]}")
    print(f"Contains \\r\\r\\n: {b'\\r\\r\\n' in raw}")
    print(f"Contains \\r\\n\\r\\n: {b'\\r\\n\\r\\n' in raw}")
    print(f"Contains \\n\\n: {b'\\n\\n' in raw}")
    print(f"Contains \\r\\n: {b'\\r\\n' in raw}")
else:
    print("CSS file does not exist")
