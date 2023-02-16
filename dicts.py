#!/usr/bin/env python
# -*- coding: utf-8 -*-

# lisence
# Copyright 2018 PokestarFan
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

dna_dict = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C'
}

rna_dict = {
    'A': 'U',
    'U': 'A',
    'C': 'G',
    'G': 'C'
}

amino_acids = { #data from http://www.science.oregonstate.edu/genbio/otherresources/aminoacidtranslation.htm
    'AAA': 'Lysine',
    'AAU':'Asparagine',
    'AUU':'Isoleucine',
    'ACU':'Threonine',
    'AGU':'Serine',
    'AAC':'Asparagine',
    'AUC':'Isoleucine',
    'ACC':'Threonine',
    'AGC':'Serine',
    'AG':'Lysine',
    'AUG':'Methionine',
    'ACG':'Threonine',
    'AGG':'Arginine',
    'UAA':'Stop Codon',
    'UUA':'Leucine',
    'UCA':'Serine',
    'UGA':'Stop Codon',
    'UAU':'Tyrosine',
    'UUU':'Phenylalanine',
    'UCU':'Serine',
    'UGU':'Cysteine',
    'UAC':'Tyrosine',
    'UUC':'Phenylalanine',
    'UCC':'Serine',
    'UGC':'Cysteine',
    'UAG':'Stop Codon',
    'UUG':'Leucine',
    'UCG':'Serine',
    'UGG':'Tryptophan',
    'CAA':'Glutamine',
    'CUA':'Leucine',
    'CCA':'Proline',
    'CGA':'Arginine',
    'CAU':'Histidine',
    'CUU':'Leucine',
    'CCU':'Proline',
    'CGU':'Arginine',
    'CAC':'Histidine',
    'CUC':'Leucine',
    'CCC':'Proline',
    'CGC':'Arginine',
    'CAG':'Glutamine',
    'CUG':'Leucine',
    'CCG':'Proline',
    'CGG':'Arginine',
    'GAA':'Glutamic Acid',
    'GUA':'Valine',
    'GCA':'Alanine',
    'GGA':'Glycine',
    'GAU':'Aspartic Acid',
    'GUU':'Valine',
    'GCU':'Alanine',
    'GGU':'Glycine',
    'GAC':'Aspartic Acid',
    'GUC':'Valine',
    'GCC':'Alanine',
    'GGC':'Glycine',
    'GAG':'Glutamic Acid',
    'GUG':'Valine',
    'GCG':'Alanine',
    'GGG':'Glycine'
}
