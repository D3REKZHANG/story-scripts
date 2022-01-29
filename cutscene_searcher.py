import os;
import docx; 

s = [];

direc = str(input("Directory: "))

total = 0;

for f in os.listdir("./"+direc):
    doc = docx.Document("./"+direc+"/"+f)
    for line in doc.paragraphs:
        for run in line.runs:
            if len(run.text.split()) > 0 and run.text.split()[0] == 'Nostalgia':
                if len(run.text.split(' - ')) > 1:
                    s.append(f.split('.docx')[0] + ' ' + run.text.split(' - ')[1])
                elif len(run.text.split(' – ')) > 1:
                    s.append(f.split('.docx')[0] + ' ' + run.text.split(' – ')[1])
                else:
                    print(f)

for c in s:
    print(c)
