#!/usr/bin/env python
# -*- coding: utf-8 -*-

import PyPDF2
from PyPDF2 import PdfFileReader
import docx
import time
import sys


def pdf_metadata (filename):
    try:

    	pdfFile = PdfFileReader(file(filename, 'rb'))
        metadata = pdfFile.getDocumentInfo()
        print ' - Document: ' + str(filename)
        for meta in metadata:
            print ' - ' + meta + ':' + metadata[meta]
    except Exception as e:
        print "Exception detected in pdf_metadata " + str(e)

def doc_metadata (filename):
    try:

        docxFile = docx.Document(file(filename,'rb'))
        #Get the structure
        docxInfo = docxFile.core_properties
        #Print the metadata which it wants to display
        attribute = ["author", "category", "comments", "content_status", 
            "created", "identifier", "keywords", "language", 
            "last_modified_by", "last_printed", "modified", 
            "revision", "subject", "title", "version"]
        #run the list in a for loop to print the value of each metadata
        #print ' - Document: ' + str(fileName)
        for meta in attribute:
            metadata = getattr (docxInfo,meta)
            #value = metadata([meta])
            print "\t-" + str(meta) + ": " + str(metadata)
    except Exception as e:
        print "Exception detected in doc_metadata " + str(e)

def main (argv):
    print "Entering... "
    target = str(sys.argv[1])
    ext=target.lower().rsplit(".",1)[-1]
    if ext == "pdf":
        pdf_metadata(target)
    if ext == "doc" or ext =="docx":
        doc_metadata(target)



if __name__ == "__main__":
    main(sys.argv[1:])