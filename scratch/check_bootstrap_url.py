import urllib.request

urls = [
    "https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/css/bootstrap.min.css",
    "https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/js/bootstrap.bundle.min.js"
]

for url in urls:
    try:
        with urllib.request.urlopen(url) as response:
            print(f"{url}: {response.status}")
    except Exception as e:
        print(f"{url}: Error - {e}")
