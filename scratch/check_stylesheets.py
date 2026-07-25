import urllib.request

try:
    with urllib.request.urlopen("http://127.0.0.1:5000/") as response:
        html = response.read().decode('utf-8')
    
    # Print stylesheet links
    idx = 0
    while True:
        idx = html.find('<link', idx)
        if idx == -1:
            break
        end_idx = html.find('>', idx)
        if end_idx == -1:
            break
        link = html[idx:end_idx+1]
        if 'stylesheet' in link or 'css' in link:
            print(link)
        idx = end_idx + 1
except Exception as e:
    print(f"Error fetching home stylesheets: {e}")
