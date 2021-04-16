import fitz
import io
from PIL import Image

# file = "1710.05006.pdf"
file = "pg_0033.pdf"
pdf_file = fitz.open(file)
print(pdf_file)
for page_index in range(len(pdf_file)):

    page = pdf_file[page_index]
    # print(page)
    # print(page.getDict())
    image_list = page.getImageList()
#
    for image_index, img in enumerate(page.getImageList(), start=1):

        xref = img[0]
        # extract the image bytes
        base_image = pdf_file.extractImage(xref)
        image_bytes = base_image["image"]
        # get the image extension
        image_ext = base_image["ext"]
        # load it to PIL
        image = Image.open(io.BytesIO(image_bytes))
        print(base_image)
        # save it to local disk
        image.save(open(f"image{page_index+1}_{image_index}.{image_ext}", "wb"))
# image_list = pdf_file.getImageList()
