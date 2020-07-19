import sys
import os
from PyPDF2 import PdfFileWriter, PdfFileReader


def main():        
    if len(sys.argv) < 2:
        print("Usage: ", os.path.basename(__file__), "input_pdf output_pdf")
        return
    input_name = sys.argv[1]
    output_name = sys.argv[2]
    output_pdf = PdfFileWriter()

    with open(input_name, 'rb') as readfile:
        input_pdf = PdfFileReader(readfile)
        total_pages = input_pdf.getNumPages()
        
        # reverse file orders and also rotate counter-clockwise each page 90 degrees. 
        for page in range(total_pages - 1, -1, -1):
            pdf_page = input_pdf.getPage(page)
            pdf_page.rotateClockwise(270)
            output_pdf.addPage(pdf_page)
        
        with open(output_name, 'wb') as writefile:
            output_pdf.write(writefile)


if __name__ == "__main__":
    main()