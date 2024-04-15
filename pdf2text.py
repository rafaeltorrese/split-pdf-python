import PyPDF2

def pdf_to_text(pdf_path, text_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        num_pages = reader.numPages
        for page_num in range(num_pages):
            page = reader.getPage(page_num)
            text += page.extractText()
    with open(text_path, 'w') as text_file:
        text_file.write(text)

if __name__ == "__main__":
    pdf_path = "03_transportation.pdf"
    text_path = "03_transportation.txt"
    pdf_to_text(pdf_path, text_path)
    print("Text extracted and saved to", text_path)

