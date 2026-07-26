import urllib.request

url = "http://127.0.0.1:5000/static/images/inhouse/animation/index.html"
try:
    with urllib.request.urlopen(url) as response:
        print(f"Iframe content status: {response.status}")
        print(f"Page content size: {len(response.read())} bytes")
except Exception as e:
    print(f"Error fetching iframe content: {e}")
