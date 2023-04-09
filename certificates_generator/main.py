from reportlab.pdfgen import canvas
from PIL import Image
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
import csv

# we know some glyphs are missing, suppress warnings
import reportlab.rl_config
reportlab.rl_config.warnOnMissingFontGlyphs = 0

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('Poppins', './Poppins-Medium.ttf'))
pdfmetrics.registerFont(TTFont('PoppinsBold', './Poppins-Bold.ttf'))

purpleColor = "#7B24FF"

label_style = ParagraphStyle('Label Style',
    fontName='Poppins',
    fontSize=26,
    leading=20,
    alignment=0
)

title_style = ParagraphStyle("Title Style", 
    fontName='PoppinsBold',
    fontSize=32,
    leading=20,
    alignment=0,
    textColor=purpleColor,
)


pageWidth, pageHeight = (841.89, 595.27)

def pasteImage(c):
    template = Image.open(r"./template.png")
    c.drawImage(template.filename, 0, 0, pageWidth, pageHeight)

def pasteLabels(c):
    # Creating the labels
    label1 = Paragraph("Felicidades a", label_style)
    label2 = Paragraph("Por completar el curso", label_style)
    label3 = Paragraph("Instruido por", label_style)

    # Placing labels on pdf

    # 1
    label1.wrapOn(c, pageWidth, 50)
    label1.drawOn(c, 30, 500)

    # 2
    label2.wrapOn(c, pageWidth, 50)
    label2.drawOn(c, 30, 350)

    # 3
    label3.wrapOn(c, pageWidth, 50)
    label3.drawOn(c, 30, 200)

def pasteTitles(c, student, course, teacher):
    # Creating the labels
    student_text = Paragraph(student, title_style)
    course_text = Paragraph(course, title_style)
    teacher_text = Paragraph(teacher, title_style)

    # Placing titles on pdf

    # Student
    student_text.wrapOn(c, pageWidth, 100)
    student_text.drawOn(c, 30, 470)

    # Course
    course_text.wrapOn(c, pageWidth, 100)
    course_text.drawOn(c, 30, 320)

    # Teacher
    teacher_text.wrapOn(c, pageWidth, 100)
    teacher_text.drawOn(c, 30, 170)


def generateCertificates(student, course, teacher):
    c = canvas.Canvas(f"./certificates/{student}_{course}.pdf", pagesize=(pageWidth, pageHeight))
    c.setTitle(f"Certificate of {student} in the course {course}")

    pasteImage(c)
    pasteLabels(c)
    pasteTitles(c, student, course, teacher)
    c.showPage()
    c.save()


# Working with de data.csv
with open('./data.csv', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        generateCertificates(row[0], row[1], row[2])