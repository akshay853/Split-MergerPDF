from PyPDF2 import PdfFileMerger

def Split():
    # working on it



def Merger(pdfs):
    merger = PdfFileMerger()
    for pdf in pdfs:
        merger.append(pdf)
    merger.write("result.pdf")
    merger.close()


if __name__ == "__main__":
    pdfs = [ 'form11.pdf', 'pan.pdf','cheque.pdf', 'Aadhar.pdf']
    Merger(pdfs)