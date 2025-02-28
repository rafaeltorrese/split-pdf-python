from PyPDF2 import PdfWriter, PdfReader
from data import pathtofile, toc, chapter_start


def pdf_splitter(filename, new_filename='file', pages=(1, 1)):
    start, end = pages
    read_file = PdfReader(open(filename, 'rb'))
    new_pdf = PdfWriter()
    try:
        with open(f'{new_filename}.pdf', 'wb') as f:
            for i in range(start - 1, end):
                new_pdf.add_page(read_file.pages[i])
                new_pdf.write(f)
        print(f'{new_filename}.pdf splitted successfully')
    except Exception as e:
        print(e)

if __name__ == '__main__':        
    for i, toc in enumerate(toc.items(), chapter_start):
        name, page = toc
        my_filename = name.lower().replace(' ','-').replace(':-','_').replace('/','-')
        pdf_splitter(filename=pathtofile, 
                     new_filename=f'{str(i).zfill(2)}_{my_filename}', 
                     pages=page)