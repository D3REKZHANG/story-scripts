import os;
import docx; 

character = str(input("Character: "))

direcs = ['Act 1']#['Act 1', 'Act 2 Lilith', 'Act 2 Prim', 'Act 3 Lilith','Act 3 Prim']

expressions = {}

total = 0;

for direc in direcs:
    for f in os.listdir("./"+direc):
        doc = docx.Document("./"+direc+"/"+f)
        for line in doc.paragraphs:
            for run in line.runs:
                s = run.text.split()
                if len(s)>=3 and s[0].replace('?','').replace(':','') == character:
                    if '(' in s[1] and ')' in s[2]:
                        b1 = s[1].index('(')
                        b2 = s[2].index(')')
                        key = s[1][b1+1:] + " " + s[2][:b2]
                        if key in expressions:
                            expressions[key]+=1
                        else:
                            expressions[key]=1

expressions = dict(sorted(expressions.items(), key=lambda item: item[1],reverse=True))

for key in expressions:
    print(f"{key}: {expressions[key]}")

