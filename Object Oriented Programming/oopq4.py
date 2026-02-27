##4
class PdfDocument:
    def display(self):
        print("Displaying PDF Document.")

class WordDocument:
    def display(self):
        print("Displaying a Word document.")

def show_document(doc):
    doc.display()

doc=PdfDocument()
show_document(doc)
doc=WordDocument()
show_document(doc)
