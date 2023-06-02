import PyPDF2
# from fpdf import FPDF

with open('dictionary.txt') as translate:
    path = input('Please enter document filepath: ')

    pdf_reader  = PyPDF2.PdfReader(open(path, 'rb'))

    for page in pdf_reader.pages:
        text = page.extract_text()
        print(text, '\n') # Just for testing

        #for english, spanish in translate.items():
            #spanish_text = text.replace(english, spanish)
        
        #print(spanish_text, '\n') # Just for testing
