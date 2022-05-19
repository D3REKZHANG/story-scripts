import os,docx,re
from helper import l_sorted

s = []

direc = str(input("Directory: "))
regex = str(input("Filename Regex: "))

total = 0

for f in l_sorted(os.listdir("./"+direc)):
    if not re.match(regex, f):
        continue
    doc = docx.Document("./"+direc+"/"+f)
    subtotal = 0
    for line in doc.paragraphs:
        for run in line.runs:
            subtotal += len(run.text.split())
    print(f'{f}: {subtotal}')
    total+= subtotal

print(total)

