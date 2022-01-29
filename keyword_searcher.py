import os;
import docx; 

s = [];

direc = str(input("Directory: "))
search = str(input("Keyword: "))

total = 0;

for f in os.listdir("./"+direc):
    doc = docx.Document("./"+direc+"/"+f)
    found=False
    for line in doc.paragraphs:
        for run in line.runs:
            if search.lower() in run.text.lower() or search.lower()+'.' in run.text.lower():
                s.append(f)
                found=True
                break
        if found:
            break

for f in s:
    print(f)
