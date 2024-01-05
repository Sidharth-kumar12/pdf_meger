
import PyPDF2
from PyPDF2 import PdfMerger

pdfs = ['1.pdf.pdf', '2.pdf.pdf']

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")  # writing line
merger.close()


# Another way of importing:
from PyPDF2 import PdfMerger

# Initialize PdfMerger
merger = PdfMerger()

# Add PDF files to merge
merger.append('1.pdf.pdf')
merger.append('1.pdf.pdf')

# Save the merged PDF to a new file
merger.write('merged.pdf')

# Close the PdfMerger object
merger.close()