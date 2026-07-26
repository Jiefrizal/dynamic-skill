import os
from html.parser import HTMLParser

class SimpleHTMLValidator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.errors = []

    def handle_starttag(self, tag, attrs):
        # We ignore self-closing tags in HTML5
        self_closing = {'img', 'br', 'hr', 'input', 'meta', 'link', 'source', 'embed', 'param', 'col', 'area', 'track', 'wbr'}
        if tag not in self_closing:
            self.tags.append((tag, self.getpos()))

    def handle_endtag(self, tag):
        self_closing = {'img', 'br', 'hr', 'input', 'meta', 'link', 'source', 'embed', 'param', 'col', 'area', 'track', 'wbr'}
        if tag in self_closing:
            return
        if not self.tags:
            self.errors.append(f"Unexpected closing tag </{tag}> at line {self.getpos()[0]}, col {self.getpos()[1]}")
            return
        last_tag, pos = self.tags.pop()
        if last_tag != tag:
            self.errors.append(f"Mismatched tag: expected </{last_tag}> (opened at line {pos[0]}, col {pos[1]}), but found </{tag}> at line {self.getpos()[0]}, col {self.getpos()[1]}")
            # Try to recover by popping until we find a match or keep it
            while self.tags:
                t, p = self.tags.pop()
                if t == tag:
                    break

def check_html_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Strip Jinja control statements to avoid interfering with HTML structure, but keep block tags if needed
    # Better yet, let's keep it simple or just parse the HTML. Jinja syntax {% ... %} or {{ ... }} doesn't usually look like HTML tags, but can contain them.
    # Let's remove comments and Jinja expressions to be safe
    import re
    # Remove Jinja statements {% ... %}, {{ ... }}, {# ... #}
    content_clean = re.sub(r'\{%.*?%\}', '', content, flags=re.DOTALL)
    content_clean = re.sub(r'\{\{.*?\}\}', '', content_clean, flags=re.DOTALL)
    content_clean = re.sub(r'\{#.*?#\}', '', content_clean, flags=re.DOTALL)
    content_clean = re.sub(r'<!--.*?-->', '', content_clean, flags=re.DOTALL)

    parser = SimpleHTMLValidator()
    try:
        parser.feed(content_clean)
        parser.close()
    except Exception as e:
        return [f"Parser error: {e}"]
    
    errors = parser.errors
    if parser.tags:
        for tag, pos in parser.tags:
            errors.append(f"Unclosed tag <{tag}> opened at line {pos[0]}, col {pos[1]}")
    return errors

def main():
    templates_dir = r"c:\Users\LENOVO\OneDrive\Desktop\Dynamic Skill\company profile\templates"
    for root, dirs, files in os.walk(templates_dir):
        for file in files:
            if file.endswith('.html'):
                path = os.path.join(root, file)
                errs = check_html_file(path)
                if errs:
                    print(f"\n--- {file} ({len(errs)} problems) ---")
                    for err in errs:
                        print(err)

if __name__ == '__main__':
    main()
