from PyPDF2 import PdfFileReader
import fitz



pdf_document = "pg_0033.pdf"

doc = fitz.open(pdf_document)
page = doc.pages()
print(next(page))
print("Исходный документ: ", doc)
print(f"Количество страниц: {doc.pageCount}")
print(doc.metadata)
for current_page in range(len(doc)):
    page = doc.loadPage(current_page)

    page_text = page.getText("text")
    print(page_text)
    print("Стр. ", current_page+1)
    # print(page_text)
    file_txt = open("result.txt", "w")
    file_txt.write(page_text)