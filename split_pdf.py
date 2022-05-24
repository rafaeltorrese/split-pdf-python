from PyPDF2 import PdfFileWriter, PdfFileReader
from data import pathtofile, toc


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
    for name, page in toc.items():        
        pdf_splitter(pathtofile, name.lower().replace(' ','_'), page)