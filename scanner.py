from glob import glob
from pathlib import Path
import os
import argparse
import PyPDF2
import re
import csv

def extract_keywords(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines

def count_all_occurrences(pdf_str, keywords):
    counts = {keyword: 0 for keyword in keywords}
    for keyword in keywords:
        counts[keyword] = pdf_str.lower().count(keyword)
    return counts

def extract_text_from_pdf(pdf_file):
    with open(pdf_file, 'rb') as pdf:
        reader = PyPDF2.PdfReader(pdf, strict=False)
        text = []

        for page in reader.pages:
            content = page.extract_text()
            text.append(content)

    return text
    
if __name__ == '__main__':
    pdfs = []
    for path in Path('./').rglob('*'):
        if path.suffix.lower() == ".pdf":
            pdfs.append(path)

    keywords = extract_keywords('keywords.txt')

    with open('result1.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        field = ['article_id'] + [keyword for keyword in keywords]
        writer.writerow(field)
        for pdf in pdfs:
            extracted_text = extract_text_from_pdf(pdf)[0].replace('\n', ' ')
            counts = count_all_occurrences(extracted_text, keywords)
            filename = str(pdf)[str(pdf).rindex("\\") + 1:len(str(pdf))-4]
            row = [filename] + list(counts.values())
            writer.writerow(row)