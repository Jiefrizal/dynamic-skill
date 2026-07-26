import os

css_path = r"c:\Users\LENOVO\OneDrive\Desktop\Dynamic Skill\company profile\static\css\style.css"

def check_css(path):
    if not os.path.exists(path):
        print("CSS file does not exist")
        return
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Strip comments
    import re
    content_clean = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    
    # Check braces
    stack = []
    errors = []
    lines = content_clean.split('\n')
    
    for line_num, line in enumerate(lines, 1):
        for char_num, char in enumerate(line, 1):
            if char == '{':
                stack.append(('{', line_num, char_num))
            elif char == '}':
                if not stack:
                    errors.append(f"Unexpected closing brace '}}' at line {line_num}, col {char_num}")
                else:
                    stack.pop()
                    
    for brace, line_num, char_num in stack:
        errors.append(f"Unclosed opening brace '{{' at line {line_num}, col {char_num}")
        
    if errors:
        print(f"Found {len(errors)} problems in CSS:")
        for err in errors:
            print(err)
    else:
        print("CSS braces are perfectly balanced!")

if __name__ == '__main__':
    check_css(css_path)
