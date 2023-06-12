# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 15:28:24 2023

@author: APP
"""
import os
from io import StringIO
import PyPDF2
import re
import requests # get dictionary from github pages

class Translator:
    
    def __init__(self, language):
        '''
        Constructor for Translator object. Translator object stores dictionary
        and pdf files and performs text extraction and manipulation.

        Parameters
        ----------
        language : STRING
            The language to which the translator should map English words

        Raises
        ------
        Exception
            Raise if the requested language is not supported.

        Returns
        -------
        None.

        '''
        self.language = language
        
        if requests.get('https://evensong.github.io/unite/{}.txt'.format(self.language)).ok:
            self.online_dict = requests.get('https://evensong.github.io/unite/{}.txt'.format(self.language))
        else:  raise Exception("The language you have requested is currently not supported by Unite.\n")
        
        self.mapping = {}
        
        dict_buffer = StringIO(self.online_dict.text)
        
        for line in dict_buffer.readlines():
            english, other = line.split(':')
            self.mapping[english] = other.strip()
            
    def get_file(self, path, name): # TODO: Overload for drag 'n drop case
        '''
        

        Parameters
        ----------
        path : STRING
            Filepath to the bishop's order pdf file.
        name : STRING
            Name of the recipient.

        Returns
        -------
        None.

        '''
        self.name = name
        self.pdf = PyPDF2.PdfReader(open(path, 'rb'))
        self.english_text = ''
        for page in self.pdf.pages:
            self.english_text += page.extract_text()
        
        # Trim unnecessary clutter in text
        self.english_text = self.english_text.partition('OrderedQty\nFilled ')[2]
        self.english_text = self.english_text.partition('FOR INFORMATION ONLY')[0]
        self.english_text = self.english_text.replace('Ordered', '')
        self.english_text = self.english_text.replace('Qty', '')
        self.english_text = self.english_text.replace('Filled', '')

    
    def translate(self):
        '''
        Generate translated text and output text file to Desktop

        Returns
        -------
        None.

        '''
        text = self.english_text
        translated = text
        
        for english, translation in self.mapping.items():
            pattern = re.compile(english, flags=re.IGNORECASE)
            translated = pattern.sub(translation, text)
            text = translated
        self.translated_text = translated
            
        desktop = os.path.expanduser("~/Desktop")
        
        with open('{}/{}-translation.txt'.format(desktop, self.name), 'w+') as output:
            output.write(self.translated_text)
        
        
        
    
        
        
