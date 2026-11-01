import qrcode
import base64
from io import BytesIO


def generate_qr_code(url):
    """
    Generate QR code and return base64 string
    """

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )

    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(
        fill_color="black",
        back_color="white"
    )

    buffer = BytesIO()
    img.save(buffer, format="PNG")

    qr_code_data = base64.b64encode(
        buffer.getvalue()
    ).decode()

    return f"data:image/png;base64,{qr_code_data}"