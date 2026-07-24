import os
import re

css_path = r"c:\Users\LENOVO\OneDrive\Desktop\Dynamic Skill\company profile\static\css\style.css"

if os.path.exists(css_path):
    with open(css_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Normalize newlines
    content = content.replace('\r\n', '\n').replace('\r', '\n')
    
    # Let's perform replacements for compact spacing
    
    # 1. clients-section padding: 2.2rem 0 -> 1.5rem 0
    content = content.replace('padding: 2.2rem 0;', 'padding: 1.5rem 0;')
    
    # 2. clients-title-line margins: margin: 15px auto 20px; -> margin: 10px auto 12px;
    content = content.replace('margin: 15px auto 20px;', 'margin: 10px auto 12px;')
    
    # 3. clients-subtitle margins: margin: 0 auto 40px; -> margin: 0 auto 20px;
    content = content.replace('margin: 0 auto 40px;', 'margin: 0 auto 20px;')
    
    # 4. marquee-wrapper spacing: padding: 15px 0; -> padding: 5px 0; gap: 15px; -> gap: 8px;
    content = content.replace('padding: 15px 0;', 'padding: 5px 0;')
    content = content.replace('gap: 15px;', 'gap: 8px;')
    
    # 5. Mobile clients-section padding: 1.5rem 0 -> 1rem 0
    # Wait, we need to make sure we replace the one inside media query (width: 768px)
    # Let's do search and replace
    content = content.replace('padding: 1.5rem 0;', 'padding: 1rem 0;')
    
    # 6. Mobile clients-subtitle margin: 20px -> 12px
    content = content.replace('margin-bottom: 20px;', 'margin-bottom: 12px;')
    
    # 7. Mobile marquee-wrapper padding: 10px 0 -> 5px 0; gap: 10px -> 6px;
    content = content.replace('padding: 10px 0;', 'padding: 5px 0;')
    content = content.replace('gap: 10px;', 'gap: 6px;')

    # Restore CRLF
    restored = content.replace('\n', '\r\n')
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(restored)
    print("Success: Compact spacing applied to style.css!")
else:
    print("Error: CSS file does not exist")
