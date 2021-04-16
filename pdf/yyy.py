import fitz

pdf_document = "pg_0033.pdf"
doc = fitz.open(pdf_document)
page = doc[0]


mat = fitz.Matrix(2, 2)  # zoom factor 2 in each direction
rect = page.rect  # the page rectangle
mp = (rect.tl + rect.br) / 2  # its middle point, becomes top-left of clip
clip = fitz.Rect(mp, rect.br)  # the area we want
pix = page.get_pixmap(matrix=mat, clip=clip)
print(pix)
