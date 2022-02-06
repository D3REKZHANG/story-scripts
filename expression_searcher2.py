import os;
import docx; 

total = 0;

direcs = ['Act 1', 'Act 2 Lilith', 'Act 2 Prim', 'Act 3 Lilith','Act 3 Prim']

keywords = ['Asher', '?Asher', 'Asher:', '?Asher:']
search = 'neutral concern'

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
                if len(s)>=3 and s[0] in keywords:
                    if '(' in s[1] and ')' in s[2]:
                        b1 = s[1].index('(')
                        b2 = s[2].index(')')
                        expr = s[1][b1+1:] + " " + s[2][:b2]
                        if s[1][b1+1:] == 'excited' or s[1][b1+1:] == 'eating':
                            print("    "+f)
                            done = True
                            break
                            '''
                            if f"{s[0]} {expr}" in store:
                                store[f"{s[0]} {expr}"].add(f'{direc}/{f}')
                            else:
                                store[f"{s[0]} {expr}"] = set([f'{direc}/{f}'])
                            '''
            if done:
                break
    print()


'''
for k in store:
    print(k)
    for x in store[k]:
        print("    "+x)

    print()
'''
