import os
import sys

# Ensure pillow is installed
try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("Pillow is not installed. Installing Pillow...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    from PIL import Image, ImageDraw, ImageFont

# Define static folders
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLIENTS_DIR = os.path.join(BASE_DIR, 'static', 'images', 'clients')
os.makedirs(CLIENTS_DIR, exist_ok=True)

clients = [
    {"filename": "PT_Buana_Indo_Mobil_Trada.png", "short": "BIMT", "name": "BUANA INDO MOBIL", "color": "#0d6efd", "bg": "#e6f0fa"},
    {"filename": "PT_Aerobus_Transport_Manunggal.png", "short": "ATM", "name": "AEROBUS TRANSPORT", "color": "#0dcaf0", "bg": "#e6f8fc"},
    {"filename": "PT_Praja_Putra_Wangsa.png", "short": "PPW", "name": "PRAJA PUTRA WANGSA", "color": "#198754", "bg": "#e8f5e9"},
    {"filename": "PT_GDSK.png", "short": "GDSK", "name": "PT GDSK", "color": "#ffc107", "bg": "#fffde7"},
    {"filename": "BAZNAS.png", "short": "BZ", "name": "BAZNAS", "color": "#dc3545", "bg": "#ffebee"},
    {"filename": "Lanud_Roesmin_Noerjadin.png", "short": "LRN", "name": "LANUD R. NOERJADIN", "color": "#0d6efd", "bg": "#e3f2fd"},
    {"filename": "Klinik_Harapan_Medika.png", "short": "KHM", "name": "KLINIK HARAPAN MEDIKA", "color": "#20c997", "bg": "#e8f8f5"},
    {"filename": "DPW_PKB_Riau.png", "short": "PKB", "name": "DPW PKB RIAU", "color": "#fd7e14", "bg": "#fff3e0"},
    {"filename": "Think_Quran.png", "short": "TQ", "name": "THINK QUR'AN", "color": "#6f42c1", "bg": "#f3e5f5"},
    {"filename": "UMKM_Kecamatan_Sail_Pekanbaru.png", "short": "UMKM", "name": "UMKM SAIL PEKANBARU", "color": "#198754", "bg": "#e8f5e9"},
    {"filename": "Seminar_KUD.png", "short": "KUD", "name": "SEMINAR KUD", "color": "#d63384", "bg": "#fce4ec"},
]

def generate_logo(client):
    width, height = 240, 100
    # Create image with transparent or white background
    image = Image.new("RGBA", (width, height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    
    # Draw a nice modern card border or background
    # Let's draw a rounded background
    bg_color = client["bg"]
    border_color = client["color"]
    
    # Draw rounded rectangle
    draw.rounded_rectangle(
        [(10, 10), (width - 10, height - 10)], 
        radius=14, 
        fill=bg_color, 
        outline=border_color, 
        width=2
    )
    
    # Draw logo symbol on the left
    # Draw a circle on the left
    symbol_center = (45, 50)
    symbol_radius = 24
    draw.ellipse(
        [(symbol_center[0] - symbol_radius, symbol_center[1] - symbol_radius),
         (symbol_center[0] + symbol_radius, symbol_center[1] + symbol_radius)],
        fill=client["color"]
    )
    
    # Text drawing setup
    # Try to load a default font
    try:
        font_symbol = ImageFont.load_default()
        font_text = ImageFont.load_default()
    except:
        font_symbol = None
        font_text = None
        
    # Draw short abbreviation inside the circle
    # Since load_default() has no text size method or custom size, we will just position it manually
    draw.text((45, 50), client["short"], fill="#ffffff", anchor="mm")
    
    # Draw company name on the right
    draw.text((90, 50), client["name"], fill="#212529", anchor="lm")
    
    # Save the file
    filepath = os.path.join(CLIENTS_DIR, client["filename"])
    image.save(filepath)
    print(f"Generated logo for {client['name']} -> {filepath}")

for c in clients:
    generate_logo(c)

print("All logos generated successfully!")
