import urllib.request

try:
    with urllib.request.urlopen("http://127.0.0.1:5000/") as response:
        html = response.read().decode('utf-8')
    
    # Search for all script tags
    idx = 0
    while True:
        idx = html.find('<script', idx)
        if idx == -1:
            break
        end_idx = html.find('</script>', idx)
        if end_idx == -1:
            break
        script_content = html[idx:end_idx+9]
        if 'sentences' in script_content:
            print("Found script containing sentences:")
            print(script_content)
        idx = end_idx + 9
except Exception as e:
    print(f"Error fetching URL: {e}")
