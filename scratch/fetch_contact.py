import urllib.request

try:
    # Run in a try block to fetch /contact
    with urllib.request.urlopen("http://127.0.0.1:5000/contact") as response:
        html = response.read().decode('utf-8')
    
    # Check for "contact-card"
    card_idx = html.find('class="card contact-card')
    if card_idx != -1:
        print("Success! Found contact-card section in rendered /contact page:")
        print(html[card_idx-100 : card_idx+600])
    else:
        print("contact-card class not found in rendered HTML!")
except Exception as e:
    print(f"Error fetching contact page: {e}")
