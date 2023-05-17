import datetime
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.units import inch

def generate_invoice(client_name, client_address, client_phone, client_email, invoice_number, invoice_date, items, tax_rate):
    """Generates an invoice in PDF format."""

    doc = SimpleDocTemplate("invoice.pdf", pagesize=LETTER, rightMargin=10, leftMargin=10, topMargin=10, bottomMargin=10)

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Center', alignment=1))
    styles.add(ParagraphStyle(name='Right', alignment=2))

    story = []

    # Create the header with client information.
    story.append(Paragraph(f"<u>Invoice {invoice_number}</u>", styles['Heading1']))
    story.append(Paragraph(f"Invoice Date: {invoice_date}", styles['Normal']))
    story.append(Paragraph(f"Client Name: {client_name}", styles['Normal']))
    story.append(Paragraph(f"Client Address: {client_address}", styles['Normal']))
    story.append(Paragraph(f"Client Phone: {client_phone}", styles['Normal']))
    story.append(Paragraph(f"Client Email: {client_email}", styles['Normal']))

    # Create the table of items.
    data = [["Description", "Quantity", "Price", "Total"]]
    total = 0
    for description, quantity, price in items:
        row = [description, quantity, price, price * quantity * (1 + tax_rate)]
        data.append(row)
        total += row[-1]

    table = Table(data, [3*inch, 0.75*inch, 0.75*inch, 0.75*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),

        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),

        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0,0), (-1,-1), 1, colors.black)
    ]))
    story.append(table)

    # Add the total amount.
    story.append(Paragraph(f"Total: {total}", styles['Right']))

    # Add the footer.
    story.append(Paragraph("Thank you for your business!", styles['Center']))

    doc.build(story)

    return "invoice.pdf"

