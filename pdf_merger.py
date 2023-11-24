import glob
import os
from PyPDF2 import PdfMerger

merger = PdfMerger()

# get all files in directory
pdf_files = glob.glob('*.pdf')

# merge files
for file in pdf_files:
    if file == "#document-output.pdf":
        continue
    merger.append(file)

# write merged file
try:
    merger.write("#document-output.pdf")
    merger.close()
    print("Erfolg!")
except:
    print("Error")

# delete source files
for file in pdf_files:
    if file == "#document-output.pdf":
        continue
    os.remove(file)