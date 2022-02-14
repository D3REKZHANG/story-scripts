import os;
import docx; 

total = 0;

direcs = ['Act 1', 'Act 2 Lilith', 'Act 2 Prim']# 'Act 3 Lilith','Act 3 Prim']

char = str(input("Character: ").strip())
search = str(input("Expression: ").strip())

store = {}

for direc in direcs:
    print(direc)
    for f in os.listdir("./"+direc):
        doc = docx.Document("./"+direc+"/"+f)
        expressions = {}
        done = False
        for line in doc.paragraphs:
            for run in line.runs:
                s = run.text.split()
                if len(s)>=3 and s[0].replace('?', '').replace(':', '') == char:
                    if '(' in s[1] and ')' in s[2]:
                        b1 = s[1].index('(')
                        b2 = s[2].index(')')
                        expr = s[1][b1+1:] + " " + s[2][:b2]
                        if expr == search:
                            print("    "+f)
                            done = True
                            break
            if done:
                break
    print()
