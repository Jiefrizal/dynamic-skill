import os
import re

css_path = r"c:\Users\LENOVO\OneDrive\Desktop\Dynamic Skill\company profile\static\css\style.css"

if os.path.exists(css_path):
    with open(css_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Normalize to standard \n first
    content = content.replace('\r\n', '\n').replace('\r', '\n')
    
    # 1. Remove blank lines immediately after opening brace {
    content = re.sub(r'\{\s*\n+', '{\n', content)
    
    # 2. Remove blank lines immediately before closing brace }
    content = re.sub(r'\n+\s*\}', '\n}', content)
    
    # 3. Remove blank lines between property declarations (lines ending with ;)
    content = re.sub(r';\s*\n+', ';\n', content)
    
    # 4. Collapse 3 or more consecutive newlines anywhere to exactly 2 newlines (one empty line)
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    # Restore standard Windows CRLF line endings
    restored = content.replace('\n', '\r\n')
    
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(restored)
        
    print("Success: CSS file formatted and cleaned up successfully!")
else:
    print("CSS file does not exist")
