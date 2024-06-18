import qrcode
from django.conf import settings
import os



def generate_qr_code(memorial):
    if not hasattr(memorial, 'unique_id'):
        raise ValueError("El objeto Memorial no tiene un atributo 'unique_id'.")

    unique_id = str(memorial.unique_id)
    url = f"{settings.SITE_URL}/memorial/{memorial.id}?id={unique_id}"

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')

    # Directorio relativo para guardar la imagen del código QR
    qr_code_dir = os.path.join(settings.MEDIA_ROOT, "qr_codes")
    os.makedirs(qr_code_dir, exist_ok=True)

    # Ruta relativa para guardar la imagen del código QR
    qr_code_path = os.path.join(qr_code_dir, f"{memorial.id}_qr.png")
    
    # Guardar la imagen del código QR
    img.save(qr_code_path)

    return qr_code_path


