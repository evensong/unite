#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 21:38:11 2023

@author: evensong
"""

from translator import Translator
import tkinter as tk
from tkinter import filedialog, simpledialog

    
def main():
    interpreter = Translator('spanish') # TODO: allow other languages 
    
    # Hide basse window
    root = tk.Tk()
    root.withdraw()
    
    # Get filepath and recipient's name
    path = filedialog.askopenfilename(title="Bishop's Order File",
                                      filetypes=[('pdf file', '*.pdf')])
    name = simpledialog.askstring(title='Recipient Name', 
                                  prompt="Please enter recipient's name")
    
    interpreter.get_file(path, name)
    
    interpreter.translate()

if __name__ == '__main__':
    main()
