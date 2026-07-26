import os
import re
from html.parser import HTMLParser

class DetailedHTMLValidator(HTMLParser):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.tags = []
        self.ids = set()
        self.duplicate_ids = []
        self.mismatches = []
        self.unclosed = []
        
    def handle_starttag(self, tag, attrs):
        self_closing = {'img', 'br', 'hr', 'input', 'meta', 'link', 'source', 'embed', 'param', 'col', 'area', 'track', 'wbr'}
        if tag not in self_closing:
            self.tags.append((tag, self.getpos()))
            
        for attr_name, attr_val in attrs:
            if attr_name == 'id':
                if attr_val in self.ids:
                    self.duplicate_ids.append((attr_val, self.getpos()))
                else:
                    self.ids.add(attr_val)
                    
    def handle_endtag(self, tag):
        self_closing = {'img', 'br', 'hr', 'input', 'meta', 'link', 'source', 'embed', 'param', 'col', 'area', 'track', 'wbr'}
        if tag in self_closing:
            return
        if not self.tags:
            self.mismatches.append(f"Unexpected closing tag </{tag}> at line {self.getpos()[0]}, col {self.getpos()[1]}")
            return
        last_tag, pos = self.tags.pop()
        if last_tag != tag:
            self.mismatches.append(f"Mismatched tag: expected </{last_tag}> (opened at line {pos[0]}, col {pos[1]}), but found </{tag}> at line {self.getpos()[0]}, col {self.getpos()[1]}")
            # Recovery
            while self.tags:
                t, p = self.tags.pop()
                if t == tag:
                    break

def check_html_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Strip Jinja statements
    content_clean = re.sub(r'\{%.*?%\}', '', content, flags=re.DOTALL)
    content_clean = re.sub(r'\{\{.*?\}\}', '', content_clean, flags=re.DOTALL)
    content_clean = re.sub(r'\{#.*?#\}', '', content_clean, flags=re.DOTALL)
    content_clean = re.sub(r'<!--.*?-->', '', content_clean, flags=re.DOTALL)
    
    validator = DetailedHTMLValidator(os.path.basename(filepath))
    validator.feed(content_clean)
    validator.close()
    
    problems = []
    for err in validator.mismatches:
        problems.append(err)
    for tag, pos in validator.tags:
        problems.append(f"Unclosed tag <{tag}> opened at line {pos[0]}, col {pos[1]}")
    for id_val, pos in validator.duplicate_ids:
        problems.append(f"Duplicate ID '{id_val}' at line {pos[0]}, col {pos[1]}")
        
    return problems

def main():
    templates_dir = r"c:\Users\LENOVO\OneDrive\Desktop\Dynamic Skill\company profile\templates"
    total_problems = 0
    for root, dirs, files in os.walk(templates_dir):
        for file in files:
            if file.endswith('.html'):
                path = os.path.join(root, file)
                probs = check_html_file(path)
                if probs:
                    print(f"\n--- {file} ({len(probs)} problems) ---")
                    for p in probs:
                        print(p)
                    total_problems += len(probs)
    print(f"\nTotal HTML problems found: {total_problems}")

if __name__ == '__main__':
    main()
