"""
PDF builder service.

This module contains helper functions to convert a report into a PDF
document.  The implementation here uses ReportLab to assemble a
minimal PDF.  Real implementations should mirror the layout of the
Streamlit dashboard and include charts and styled text.
"""

from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer


def build_report_pdf(report: dict) -> bytes:
    """Generate a PDF from a report dict.

    Parameters
    ----------
    report : dict
        The report data containing metrics and blocks.

    Returns
    -------
    bytes
        PDF data encoded as a byte string.
    """
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("Relatório NutriSigno", styles["Title"]))
    elements.append(Spacer(1, 12))

    # Add summary
    summary = report.get("summary", "Resumo não disponível.")
    elements.append(Paragraph(summary, styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Add metrics
    metrics = report.get("metrics", {})
    metrics_lines = [f"{k}: {v}" for k, v in metrics.items()]
    metrics_text = "<br/>".join(metrics_lines) or "Nenhuma métrica."
    elements.append(Paragraph(metrics_text, styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Add blocks
    blocks = report.get("blocks", [])
    for block in blocks:
        block_type = block.get("type")
        text = block.get("text", "")
        if block_type == "heading":
            elements.append(Paragraph(text, styles["Heading2"]))
        else:
            elements.append(Paragraph(text, styles["Normal"]))
        elements.append(Spacer(1, 6))

    doc.build(elements)
    pdf_data = buffer.getvalue()
    buffer.close()
    return pdf_data