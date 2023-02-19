import csv
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

# Specify the path to the PDF file
pdf_path = 'result.pdf'

# Define a function to extract text from a PDF page
def extract_text(pdf_path):
    resource_manager = PDFResourceManager()
    return_string = StringIO()
    laparams = LAParams()
    device = TextConverter(resource_manager, return_string, laparams=laparams)
    with open(pdf_path, 'rb') as file:
        interpreter = PDFPageInterpreter(resource_manager, device)
        for page in PDFPage.get_pages(file):
            interpreter.process_page(page)
    device.close()
    return return_string.getvalue()

# Extract text from the PDF file
pdf_text = extract_text(pdf_path)

# Convert the text into a CSV file
csv_path = 'result.csv'
with open(csv_path, 'w', newline='') as file:
    writer = csv.writer(file)
    for line in pdf_text.split('\n'):
        print('proccessing......')
        writer.writerow(line.split(','))

print('done')