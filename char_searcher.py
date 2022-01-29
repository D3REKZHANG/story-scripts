import os;
import docx; 

s = [];

direc = str(input("Directory: "))
n= int(input("# of char:"))
searches = []
for i in range(n):
    searches.append(str(input("Character: ")))

total = 0;

for f in os.listdir("./"+direc):
    doc = docx.Document("./"+direc+"/"+f)
    found = []
    for line in doc.paragraphs:
        for run in line.runs:
            for search in searches:
                if search in found:
                    continue
                if search.lower() in run.text.lower().split() or search.lower()+'.' in run.text.lower().split():
                    found.append(search)
                if len(found) == len(searches):
                    s.append(f)
                    break
        if len(found) == len(searches):
            break

for f in s:
    print(f)
