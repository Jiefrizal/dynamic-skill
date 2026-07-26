import os

def check_files():
    workspace = r"c:\Users\LENOVO\OneDrive\Desktop\Dynamic Skill\company profile"
    extensions = {'.html', '.css', '.js', '.py', '.txt', 'Procfile'}
    
    corrupted_files = []
    
    for root, dirs, files in os.walk(workspace):
        if 'venv' in root or '.git' in root or '__pycache__' in root:
            continue
        for file in files:
            ext = os.path.splitext(file)[1]
            if ext in extensions or file == 'Procfile':
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'rb') as f:
                        content = f.read()
                    if b'\r\r\n' in content:
                        count = content.count(b'\r\r\n')
                        corrupted_files.append((filepath, count))
                except Exception as e:
                    print(f"Error reading {file}: {e}")
                    
    if corrupted_files:
        print(f"Found {len(corrupted_files)} files with \\r\\r\\n:")
        for path, count in corrupted_files:
            print(f"- {path}: {count} occurrences")
    else:
        print("No files with \\r\\r\\n found!")

if __name__ == '__main__':
    check_files()
