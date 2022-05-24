from operator import imod
import sys
import os
from PyPDF2 import PdfFileWriter, PdfFileReader



filename = r'C:\Users\rafael.torrese\Documents\ebooks\optimization_modelling\Optimization_Modelling_A_Practical_Approach.pdf'
new_filename = 'toc.pdf'
start, end = 6, 15

with open(filename, 'rb') as f:
    read_file = PdfFileReader(f)
new_pdf = PdfFileWriter()

with open(new_filename, 'wb') as f:
    for i in range(start - 1, end + 1):
        new_pdf.addPage(read_file.getPage(i))
        new_pdf.write(f)



