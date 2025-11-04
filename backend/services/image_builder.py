"""
Image builder service.

Generates shareable images from report data.  The stub below uses
Pillow to create a simple image with the report summary.  Real
implementations should apply the NutriSigno palette based on the
element of the user's sign and include other decorative elements.
"""

from io import BytesIO
from typing import Tuple

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    # Pillow is not installed in this environment; define a dummy
    Image = None
    ImageDraw = None
    ImageFont = None


def get_palette(elemento: str) -> Tuple[int, int, int]:
    """Return an RGB tuple based on the sign element.

    Parameters
    ----------
    elemento : str
        Element of the sign (fogo, terra, ar, agua).

    Returns
    -------
    Tuple[int, int, int]
        RGB color tuple.
    """
    palette = {
        "fogo": (231, 76, 60),  # red
        "terra": (39, 174, 96),  # green
        "ar": (52, 152, 219),  # blue
        "agua": (142, 68, 173),  # purple
    }
    return palette.get(elemento, (0, 0, 0))


def build_report_image(report: dict, element: str = "fogo") -> bytes:
    """Generate a PNG image from report data.

    Parameters
    ----------
    report : dict
        Report data including summary and metrics.
    element : str
        Element of the sign, used to choose a background colour.

    Returns
    -------
    bytes
        PNG image data.
    """
    if Image is None:
        raise RuntimeError("Pillow is not installed; cannot build images.")
    width, height = 1080, 1350
    bg_color = get_palette(element)
    img = Image.new("RGB", (width, height), color=bg_color)
    draw = ImageDraw.Draw(img)
    # Attempt to load a default font; fall back to built-in font on error
    try:
        font = ImageFont.truetype("arial.ttf", 48)
    except Exception:
        font = ImageFont.load_default()
    y = 50
    draw.text((50, y), "Relatório NutriSigno", fill=(255, 255, 255), font=font)
    y += 60
    summary = report.get("summary", "Relatório gerado.")
    draw.text((50, y), summary, fill=(255, 255, 255), font=font)
    y += 60
    metrics = report.get("metrics", {})
    for key, value in metrics.items():
        draw.text((50, y), f"{key}: {value}", fill=(255, 255, 255), font=font)
        y += 40
    # Encode as PNG
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    image_data = buffer.getvalue()
    buffer.close()
    return image_data