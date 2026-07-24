import os

css_path = r"c:\Users\LENOVO\OneDrive\Desktop\Dynamic Skill\company profile\static\css\style.css"

target = """@media (max-width:768px){

    .hero{

        min-height:auto;
        height:auto;

        display:flex;
        justify-content:flex-end;
        align-items:center;

        padding-top:90px;
        padding-bottom:15px;

        background-size:100% auto;
        background-repeat:no-repeat;
        background-position:top center;
    }

    .hero-content{

        margin-top:220px;   /* sesuaikan dengan tinggi gambar */
        width:100%;
        padding:0 15px;
    }

    .hero-title{

        font-size:1.15rem;
        font-weight:700;
        line-height:1.35;
        margin:0;
    }

    .stats-section{

        margin-top:0;
        padding-top:5px !important;
    }

    width: 28px;
    height: 28px;
    fill: currentColor;
    flex-shrink: 0;
}

.whatsapp-label {
    font-family: 'Montserrat', sans-serif;
    font-size: 14px;
    font-weight: 600;
    white-space: nowrap;
}

@media (max-width: 576px) {
    .floating-whatsapp {
        bottom: 20px;
        right: 20px;
        padding: 10px 16px;
        gap: 8px;
    }
    .floating-whatsapp svg {
        width: 22px;
        height: 22px;
    }
    .whatsapp-label {
        font-size: 12px;
    }
}"""

replacement = """@media (max-width:768px){

    .hero{

        min-height:auto;
        height:auto;

        display:flex;
        justify-content:flex-end;
        align-items:center;

        padding-top:90px;
        padding-bottom:15px;

        background-size:100% auto;
        background-repeat:no-repeat;
        background-position:top center;
    }

    .hero-content{

        margin-top:220px;   /* sesuaikan dengan tinggi gambar */
        width:100%;
        padding:0 15px;
    }

    .hero-title{

        font-size:1.15rem;
        font-weight:700;
        line-height:1.35;
        margin:0;
    }

    .stats-section{

        margin-top:0;
        padding-top:5px !important;
    }

}

/* ==================================================
   FLOATING WHATSAPP BUTTON ACCENTS
================================================== */
.floating-whatsapp svg {
    width: 28px;
    height: 28px;
    fill: currentColor;
    flex-shrink: 0;
}

.whatsapp-label {
    font-family: 'Montserrat', sans-serif;
    font-size: 14px;
    font-weight: 600;
    white-space: nowrap;
}

@media (max-width: 576px) {
    .floating-whatsapp {
        bottom: 20px;
        right: 20px;
        padding: 10px 16px;
        gap: 8px;
    }
    .floating-whatsapp svg {
        width: 22px;
        height: 22px;
    }
    .whatsapp-label {
        font-size: 12px;
    }
}

/* ==================================================
   NAMA PERUSAHAAN DI DALAM NAVBAR
================================================== */
.company-name-inline {
    font-family: 'Montserrat', sans-serif;
    white-space: nowrap;
    display: flex;
    flex-direction: column;
    line-height: 1.25;
}

.company-name-inline .company-line1 {
    font-size: 11px;
    font-weight: 700;
    color: #1a1a1a;
    letter-spacing: 0.5px;
    transition: color 0.4s ease;
}

.company-name-inline .company-line2 {
    font-size: 9.5px;
    font-weight: 800;
    letter-spacing: 1.5px;
    color: #0d6efd;
    text-transform: uppercase;
    transition: color 0.4s ease;
}

.navbar.scrolled .company-name-inline .company-line1 {
    color: #ffffff;
}

.navbar.scrolled .company-name-inline .company-line2 {
    color: #ffc107;
}

@media (max-width: 576px) {
    .company-name-inline .company-line1 {
        font-size: 9px;
    }
    .company-name-inline .company-line2 {
        font-size: 7.5px;
        letter-spacing: 1px;
    }
}"""

if os.path.exists(css_path):
    with open(css_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Normalize line endings to do comparison
    norm_content = content.replace('\r\n', '\n')
    norm_target = target.replace('\r\n', '\n')
    norm_replacement = replacement.replace('\r\n', '\n')
    
    if norm_target in norm_content:
        new_content = norm_content.replace(norm_target, norm_replacement)
        # Restore CRLF line endings
        new_content = new_content.replace('\n', '\r\n')
        with open(css_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Success: CSS file updated successfully!")
    else:
        print("Error: Target content not found in CSS file")
else:
    print("Error: CSS file does not exist")
