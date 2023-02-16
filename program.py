#!/usr/bin/env python
# -*- coding: utf-8 -*-

# lisence
# Copyright 2018 PokestarFan
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#tkinter setup
try:
    import tkinter as tk  # for python 3
except:
    import Tkinter as tk  # for python 2

#get dicts
import dicts

#conversion
def dna_to_rna(dna):
    newstring = ''
    dna = dna.upper()
    for i in dna:
        if i == 'T':
            newstring += 'U'
        else:
            newstring += i
    return newstring

def rna_to_dna(rna):
    newstring = ''
    rna = rna.upper()
    for i in rna:
        if i == 'U':
            newstring += 'T'
        else:
            newstring += i
    return newstring


#opposites
def get_amino_acids(rna):
    codons = []
    count = 0
    adder = ''
    amino_acids = ''
    rna = rna.upper()
    if 'T' in rna:
        rna = dna_to_rna(dna)
    for i in rna:
        count = 1
        added += i
        if count == 3:
            codons.append(added)
            count = 0
            adder = ''
    for codon in codons:
        assert len(codon) == 3
        amino_acid = dicts.amino_acids[codon].upper()[0:3]
        if amino_acid == 'STO':
            amino_acid = 'STOP'
        amino_acids += amino_acid
    return amino_acids


#the tkinter

def get_text():


root = tk.Tk()

en = tk.Entry(root)
en.pack()
en.focus_set()
menu_list = tk.Menu(root, name = 'options')
menu_list.add_command(label = 'DNA -> RNA', command = dna_to_rna(text))
menu_list.add_command(label = 'RNA -> DNA', command = rna_to_dna(text))
menu_list.add_command(label = 'DNA/RNA -> Amino acid', command = get_amino_acids(text))
