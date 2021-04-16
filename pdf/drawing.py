import fitz
import io
from PIL import Image

doc = "pg_0033.pdf"
pdf_file = fitz.open(doc)

page = pdf_file[0]

paths = page.get_drawings()

outpdf = fitz.open()
outpage = outpdf.new_page(width=page.rect.width, height=page.rect.height)
shape = outpage.new_shape()

for path in paths[42:]:

    for item in path["items"]:
        if item[0] == "l":
            shape.draw_line(item[1], item[2])
        elif item[0] == "re":
            shape.draw_rect(item[1])
        elif item[0] == "c":
            shape.draw_bezier(item[1], item[2], item[3], item[4])
        else:
            raise ValueError("unhandled drawing", item)

    shape.finish(
        fill=path["fill"],
        color=path["color"],
        dashes=path["dashes"],
        even_odd=path["even_odd"],
        closePath=path["closePath"],
        lineJoin=path["lineJoin"],
        lineCap=max(path["lineCap"]),
        width=path["width"],
        stroke_opacity=path["opacity"],
        fill_opacity=path["opacity"]
        )
shape.commit()
outpdf.save("drawings-page-0.pdf")
