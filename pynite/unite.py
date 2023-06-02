import PyPDF2
import codecs # for spanish characters
import re
# from fpdf import FPDF

#read english/spanish word pairs
dictionary = {}
with codecs.open('dictionary.txt', encoding='utf-8') as translate:
    
    for line in translate:
        english, spanish = line.split(':')
        dictionary[english] = spanish.strip()

        
path = input('Please enter document filepath: ')

pdf_reader  = PyPDF2.PdfReader(open(path, 'rb'))

text = ''
spanish_text = ''    
for page in pdf_reader.pages:
    text += page.extract_text()

for english, spanish in dictionary.items():
        pattern = re.compile(english, flags=re.IGNORECASE)
        spanish_text = pattern.sub(spanish, text)
        
print(spanish_text, '\n') # Just for testing
