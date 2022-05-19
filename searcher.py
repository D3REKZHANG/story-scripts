import os
import docx;

direcs = ['Act 1', 'Act 2 Lilith', 'Act 2 Prim', 'Act 3 Lilith','Act 3 Prim']

m = 0
mdoc = ''
for direc in direcs:
    for f in os.listdir("./"+direc):
        doc = docx.Document("./"+direc+"/"+f)
        total = 0
        for line in doc.paragraphs:
            for run in line.runs:
                total += len(run.text.split())

        if total > m:
            m = total
            mdoc = direc + '/' + f

print(mdoc)
print(m)
