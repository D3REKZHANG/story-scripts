import os;
import docx; 

#character = str(input("Character: "))

characters = ["Mara", 'Lilith', 'Prim', 'Asher', 'Petra', 'Teacher', 'Mom', 'Kari', 'Iris', 'Mick', 'Roxy', 'Petrov', 'Greta', 'Lilith\'sDad', 'Lilith\'s Aunt']

direcs = ['Act 1']

total = 0;

mode = int(input("1. Full Expression\n2. Pose\nSelect 1 or 2: "))

for char in characters:
    expressions = {}
    print(char + ":")
    for direc in direcs:
        for f in os.listdir("./"+direc):
            doc = docx.Document("./"+direc+"/"+f)
            for line in doc.paragraphs:
                for run in line.runs:
                    s = run.text.split()
                    if len(s) >=3:
                        x = 0
                        if s[0] == 'Lilith’s':
                            x=1
                            _char = 'Lilith\'s Aunt'
                            if len(s) < 4:
                                continue
                        else:
                            _char = s[0].replace('?', '').replace(':','')
                        if _char == char:
                            if '(' in s[x+1] and ')' in s[x+2]:
                                b1 = s[x+1].index('(')
                                b2 = s[x+2].index(')')
                                if(mode == 1):
                                    key = s[x+1][b1+1:] + " " + s[x+2][:b2]
                                else:
                                    key = s[x+1][b1+1:]
                                if key in expressions:
                                    expressions[key]+=1
                                else:
                                    expressions[key]=1

    expressions = dict(sorted(expressions.items(), key=lambda item: item[1],reverse=True))

    for key in expressions:
        print(f"{key:<40} {expressions[key]}")

    print('\n---------------------\n')

