import os;
import docx; 


chars = ['Mara', 'Lilith', 'Prim', 'Petra', 'Mom', 'Asher', 'Teacher', 'Mick', 'Iris', 'Aunt', 'Petrov', 'Greta' ]
direcs = ['Act 3 Lilith']#['Act 1', 'Act 2 Lilith', 'Act 2 Prim', 'Act 3 Lilith','Act 3 Prim']

s = {char:[] for char in chars}

for char in chars:
    for direc in direcs:
        for f in os.listdir("./"+direc):
            doc = docx.Document("./"+direc+"/"+f)
            done = False
            for line in doc.paragraphs:
                for run in line.runs:
                    text = run.text.lower()
                    if char.lower()+":" in text:
                        s[char].append(f)
                        done = True
                        break
                if done:
                    break

def getNum(s):
    n = ""
    for c in s:
        if c.isdigit():
            n+=c
    return int(n)

for char in s:
    print(char)
    l = sorted(s[char], key=lambda x: getNum(x))
    for f in l:
        print(f"    {f}")
    print()
