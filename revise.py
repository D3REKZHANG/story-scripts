import docx, os

c = {}
with open('expression_revisions.txt') as f:
    for line in f:
        line = line.strip().split('->')
        c[line[0].strip()] = line[1].strip()

direcs = ['Act 1', 'Act 2 Lilith', 'Act 2 Prim', 'Act 3 Lilith','Act 3 Prim']

for direc in direcs:
    for f in os.listdir("./"+direc):
        doc = docx.Document("./"+direc+"/"+f)
        for line in doc.paragraphs:
            for run in line.runs:
                s = run.text.split()
                if len(s)>=3:
                    if '(' in s[1] and ')' in s[2]:
                        b1 = s[1].index('(')
                        b2 = s[2].index(')')
                        expr = f"{s[0]} ({s[1][b1+1:]} {s[2][:b2]})"
                        if expr in c:
                            text = run.text.split(":")[1]
                            print(run.text)
                            run.text = c[expr]+":"+text
                            print(run.text)
        doc.save("./"+direc+"/"+f)


