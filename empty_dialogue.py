import os;
import docx; 

direcs = ['Act 1', 'Act 2 Lilith', 'Act 2 Prim', 'Act 3 Lilith','Act 3 Prim']

acts = {
    'Act 1': [],
    'Act 2 Lilith': [],
    'Act 2 Prim': [],
    'Act 3 Lilith': [],
    'Act 3 Prim': []
}

total = 0;

for direc in direcs:
    for f in os.listdir("./"+direc):
        if '~' in f:
            continue
        doc = docx.Document("./"+direc+"/"+f)
        contains = False
        for line in doc.paragraphs:
            for run in line.runs:
                s = run.text.split()
                if len(s)>=3:
                    if '(' in s[1] and ')' in s[2]:
                        b1 = s[1].index('(')
                        b2 = s[2].index(')')
                        expr = s[1][b1+1:] + " " + s[2][:b2]
                        if len(s) == 3:
                            contains = True
                            break
            if contains:
                break

        if not contains:
            acts[direc].append(f[6:f.index(".")])
        else:
            print(f"{direc}/{f}")

def find_char(s):
    for i in range(len(s)):
        if s[i] < '0' or s[i] > '9':
            return i

for act in acts:
    print(act)
    l = acts[act]
    l = sorted(l, key = lambda x : int(x[:find_char(x)]))
    for f in l:
        print("   Scene "+f)
