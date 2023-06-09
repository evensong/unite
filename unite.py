import os
import PyPDF2
import codecs # for spanish characters
import re
import requests # get dictionary from github pages

dictionary = {}

# get updated dictionary from the web, then read in word mapping
response = requests.get('https://evensong.github.io/unite/dictionary.txt')

with open('english-spanish.txt', 'w+') as update:
    update.write(response.text)
    
with codecs.open('english-spanish.txt', encoding='utf-8') as translate:
    
    for line in translate:
        english, spanish = line.split(':')
        dictionary[english] = spanish.strip()
        
# Read in the PDF        
path = input('Please enter document filepath: ')

pdf_reader  = PyPDF2.PdfReader(open(path, 'rb'))

# Extract Text from PDF
text = ''
spanish_text = ''    
for page in pdf_reader.pages:
    text += page.extract_text()

# Remove header and footer text to declutter output
text = text.partition('OrderedQty\nFilled ')[2]
text = text.partition('FOR INFORMATION ONLY')[0]
text = text.replace('Ordered', '')
text = text.replace('Qty', '')
text = text.replace('Filled', '')

# Replace English with Spanish based on the dictionary file
for english, spanish in dictionary.items():
        pattern = re.compile(english, flags=re.IGNORECASE)
        spanish_text = pattern.sub(spanish, text)
        text = spanish_text
        
#print(spanish_text, '\n') # Just for testing

desktop = os.path.expanduser("~/Desktop")
name = input('Please enter order recipient\'s name: ')
with open('{}/{}-translation.txt'.format(desktop, name), 'w+') as output:
    output.write(spanish_text)

