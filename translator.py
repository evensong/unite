# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 15:28:24 2023

@author: APP
"""
import os
import PyPDF2
import codecs # for spanish characters
import re
import requests # get dictionary from github pages

class Translator:
    
    def __init__(self, language, document):
        self.language = language
        self.document = document
        if requests.get('https://evensong.github.io/unite/dictionary.txt').ok:
            self.live_dict = requests.get('https://evensong.github.io/unite/dictionary.txt')
        else:  raise Exception("Error connecting to online dictionary.\n")
        
        self.mapping = {}
    
        
        