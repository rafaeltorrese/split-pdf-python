from operator import imod
import sys
import os
from PyPDF2 import PdfFileWriter, PdfFileReader



pathtofile = r'C:\Users\rafael.torrese\Documents\ebooks\optimization_modelling\Optimization_Modelling_A_Practical_Approach.pdf'

def pdf_splitter(filename, new_filename='file', pages=(1, 1)):
    start, end = pages
    read_file = PdfFileReader(open(filename, 'rb'))
    new_pdf = PdfFileWriter()
    try:
        with open(f'{new_filename}.pdf', 'wb') as f:
            for i in range(start - 1, end):
                new_pdf.addPage(read_file.getPage(i))
                new_pdf.write(f)
        print('PDF splitted successfully')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    # pdf_splitter(pathtofile, 'toc', (6,14))  
    toc ={
        "01 Introduction": (36,48),
        "02 The Process of Optimization": (50,63),
        "04 Simple Modelling Techniques I": (92, 135),
        "05 Simple Modelling Techniques II":(136, 176),
        "06 Modelling Well Known Problems II":(178, 208),
        "07 Modelling Well Known Problems II":(210, 236),
        "08 Alternative Modelling":(238, 253),
        "09 Solution Approaches An Overview":(256, 285),
        "10 Input Preparation and Model Solving":(310,341),
        "11 Output Analysis and Practical Issues":(360, 379),
        "12 Basic Optimization Techniques":(380,410),
        "13 Models for Practical Problems I":(414,442),
        "14 Models for Practical Problems II":(444,468),
        "15 Solving Practical Problems":(470,491),
    }

    for name, page in toc.items():        
        pdf_splitter(pathtofile, name.lower().replace(' ','_'), page)