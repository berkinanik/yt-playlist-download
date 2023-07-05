import PyPDF2
import re


def extractLinksFromPDF(pdfFile):
    PDFFile = open(pdfFile, "rb")

    PDF = PyPDF2.PdfFileReader(PDFFile)
    pages = PDF.getNumPages()
    key = "/Annots"
    uri = "/URI"
    ank = "/A"

    urls = []

    for page in range(pages):
        pageSliced = PDF.getPage(page)
        pageObject = pageSliced.getObject()
        if pageObject is None:
            continue
        if key in pageObject.keys():
            ann = pageObject[key]
            for a in ann:
                u = a.getObject()
                if uri in u[ank].keys():
                    urls.append(u[ank][uri])

    pattern = re.compile(
        "^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube(-nocookie)?\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$"
    )

    return [url for url in urls if pattern.match(url)]
