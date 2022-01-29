import os,docx,re

s = []

direc = str(input("Directory: "))
regex = str(input("Filename Regex: "))

total = 0

for f in os.listdir("./"+direc):
    if not re.match(regex, f):
        continue
    print(f)
    doc = docx.Document("./"+direc+"/"+f)
    for line in doc.paragraphs:
        for run in line.runs:
            total += len(run.text.split())

print(total)

