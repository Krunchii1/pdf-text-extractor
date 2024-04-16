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
    if not os.path.exists(pdf_file):
        print("Error: File does not exist")
        return None
    
    if os.path.getsize(pdf_file) == 0:
        print("Error: File is empty")
        return 1
    
    try:
        with open(pdf_file, 'rb') as pdf:
            reader = PyPDF2.PdfReader(pdf, strict=False)
            text = []

            for page in reader.pages:
                text.append(page.extract_text())

        return text
    except Exception as e:
        print("Error:", e)
        return None
    
if __name__ == '__main__':
    pdfs = []
    errors = []
    for path in Path('./').rglob('*'):
        if path.suffix.lower() == ".pdf":
            pdfs.append(path)

    keywords = extract_keywords('keywords.txt')

    with open('result1.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        field = ['article_id'] + [keyword for keyword in keywords]
        writer.writerow(field)
        for pdf in pdfs:
            extracted_text = extract_text_from_pdf(pdf)
            if extracted_text == 1:
                errors.append(pdf)
                continue
            extracted_text = ' '.join(extracted_text).replace('\n', ' ')
            counts = count_all_occurrences(extracted_text, keywords)
            filename = str(pdf)[str(pdf).rindex("\\") + 1:len(str(pdf))-4]
            print('Scanning:', pdf)
            row = [pdf] + list(counts.values())
            writer.writerow(row)

    print(errors)