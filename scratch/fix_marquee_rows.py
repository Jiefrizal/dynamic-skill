import os
import re

css_path = r"c:\Users\LENOVO\OneDrive\Desktop\Dynamic Skill\company profile\static\css\style.css"

if os.path.exists(css_path):
    with open(css_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Normalize newlines
    content = content.replace('\r\n', '\n').replace('\r', '\n')
    
    # 1. Update marquee-wrapper to stack rows
    wrapper_pattern = r"\.marquee-wrapper\s*\{\s*overflow:\s*hidden;\s*position:\s*relative;\s*width:\s*100\%\s*;\s*padding:\s*15px\s*0;\s*\}"
    # Wait, let's look at lines 1145-1150 in the previous check:
    # 1145: .marquee-wrapper {
    # 1146:     overflow: hidden;
    # 1147:     position: relative;
    # 1148:     width: 100%;
    # 1149:     padding: 15px 0;
    # 1150: }
    wrapper_target = """.marquee-wrapper {
    overflow: hidden;
    position: relative;
    width: 100%;
    padding: 15px 0;
}"""
    wrapper_replacement = """.marquee-wrapper {
    overflow: hidden;
    position: relative;
    width: 100%;
    padding: 15px 0;
    display: flex;
    flex-direction: column;
    gap: 15px;
}"""
    
    # 2. Update keyframes and reverse animation
    keyframes_target = """@keyframes marqueeScroll {
    0% {
        transform: translateX(0);
}
    100% {
        transform: translateX(-50%);
}
}"""
    keyframes_replacement = """@keyframes marqueeScroll {
    0% {
        transform: translateX(0);
}
    100% {
        transform: translateX(-50%);
}
}

.marquee-reverse {
    animation: marqueeScrollReverse 25s linear infinite;
}

@keyframes marqueeScrollReverse {
    0% {
        transform: translateX(-50%);
}
    100% {
        transform: translateX(0);
}
}"""

    # Do the replacements
    content_norm = content
    if wrapper_target in content_norm:
        content_norm = content_norm.replace(wrapper_target, wrapper_replacement)
        print("Success: Updated .marquee-wrapper")
    else:
        print("Warning: .marquee-wrapper target not found exactly. Searching using regex...")
        content_norm = re.sub(
            r"\.marquee-wrapper\s*\{\s*overflow:\s*hidden;\s*position:\s*relative;\s*width:\s*100\s*%;\s*padding:\s*15px\s*0;\s*\}",
            wrapper_replacement,
            content_norm
        )
        
    if keyframes_target in content_norm:
        content_norm = content_norm.replace(keyframes_target, keyframes_replacement)
        print("Success: Updated keyframes")
    else:
        print("Warning: Keyframes target not found exactly. Searching using regex...")
        content_norm = re.sub(
            r"@keyframes\s*marqueeScroll\s*\{\s*0\%\s*\{\s*transform:\s*translateX\(0\);\s*\}\s*100\%\s*\{\s*transform:\s*translateX\(-50\%\);\s*\}\s*\}",
            keyframes_replacement,
            content_norm
        )
        
    # Also adjust responsive wrapper gap
    responsive_target = """.marquee-wrapper {
        padding: 10px 0;
}"""
    responsive_replacement = """.marquee-wrapper {
        padding: 10px 0;
        gap: 10px;
}"""
    if responsive_target in content_norm:
        content_norm = content_norm.replace(responsive_target, responsive_replacement)
        print("Success: Updated responsive gap")
        
    # Write back
    restored = content_norm.replace('\n', '\r\n')
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(restored)
    print("CSS file updated successfully!")
else:
    print("Error: CSS file does not exist")
