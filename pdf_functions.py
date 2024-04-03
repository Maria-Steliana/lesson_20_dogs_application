import reportlab
from reportlab.pdfgen import canvas


def create_pdf(path: str, image_path: str = "images\\image_1712159993.png"):
    new_pdf = canvas.Canvas("test.pdf")

    new_pdf.drawString(250,500,"Imagine aici")
    new_pdf.drawImage(image_path, x=200, y=200)
    new_pdf.save()
