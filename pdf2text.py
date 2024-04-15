import os
import PyPDF2
import textwrap


def pdf_to_text(pdf_path, wrap_width=200):
    base_filename = os.path.basename(pdf_path)
    filename, _ = os.path.splitext(base_filename) 
    text_path = f'{filename}.txt'
    wrapped_text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        num_pages = reader.numPages
        for page_num in range(num_pages):
            page = reader.getPage(page_num)
            extracted_text = page.extractText()
            wrapped_text += textwrap.fill(extracted_text, width=wrap_width)
            wrapped_text += "\n\n"  # Adding empty lines between pages
    with open(text_path, 'w') as text_file:
        text_file.write(wrapped_text)
    return text_path

        
if __name__ == "__main__":
    pdf_path = "09-moving-average-smoothing.pdf"
    max_column_width = 200  # Set your desired maximum column width here
    text_path = pdf_to_text(pdf_path, wrap_width=max_column_width)
    print("Wrapped text extracted and saved to", text_path)
