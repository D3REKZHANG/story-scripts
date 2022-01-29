import os;
import docx; 

character = str(input("Character: "))
total = 0;

direcs = ['Act 1', 'Act 2 Lilith', 'Act 2 Prim', 'Act 3 Lilith','Act 3 Prim']

for direc in direcs:
    for f in os.listdir("./"+direc):
        doc = docx.Document("./"+direc+"/"+f)
        expressions = {}
        for line in doc.paragraphs:
            for run in line.runs:
                s = run.text.split()
                if len(s)>=3 and s[0] == character:
                    if '(' in s[1] and ')' in s[2]:
                        key = s[1][1:]+" "+s[2][:-2]
                        if key in expressions:
                            expressions[key]+=1
                        else:
                            expressions[key]=1
        search = ['on phone']
        tf = True
        for expr in search:
            if expr not in expressions:
                tf = False
        if tf:
            print(direc + ' ' +f)

