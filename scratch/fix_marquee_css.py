import os
import re

css_path = r"c:\Users\LENOVO\OneDrive\Desktop\Dynamic Skill\company profile\static\css\style.css"

if os.path.exists(css_path):
    with open(css_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # We want to find `.client-logo-card:hover { ... }` around line 1145
    # Let's search using a regex that handles newlines and spacing robustly
    pattern = r"\.client-logo-card:hover\s*\{\s*100\%\s*\{\s*transform:\s*translateX\(-50\%\);\s*\}\s*\}"
    
    match = re.search(pattern, content)
    if match:
        print(f"Found match: {match.group(0)}")
        
        replacement = """.client-logo-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.08) !important;
    border-color: rgba(13, 110, 253, 0.2);
}

.client-logo {
    max-height: 50px;
    max-width: 100%;
    object-fit: contain;
    transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

.client-logo-card:hover .client-logo {
    transform: scale(1.05);
}

@keyframes marqueeScroll {
    0% {
        transform: translateX(0);
    }
    100% {
        transform: translateX(-50%);
    }
}"""
        
        # Replace the matched text
        new_content = content[:match.start()] + replacement + content[match.end():]
        
        with open(css_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Success: Marquee CSS fixed and updated successfully!")
    else:
        print("Error: Could not find target content using regex")
        # Let's print the tail of the CSS to see what is there
        print(repr(content[-300:]))
else:
    print("Error: CSS file does not exist")
