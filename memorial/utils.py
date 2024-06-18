import qrcode
from django.conf import settings
import os



def generate_qr_code(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    
    qr_code_dir = os.path.join(settings.MEDIA_ROOT, "qr_codes")
    os.makedirs(qr_code_dir, exist_ok=True)
    
    qr_code_path = os.path.join(qr_code_dir, "memorial_qr.png")
    
    img.save(qr_code_path)

    return qr_code_path