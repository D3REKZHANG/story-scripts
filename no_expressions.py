import os;
import docx; 
from helper import l_sorted;

total = 0;

direcs = ['Act 3 Lilith']

characters = ["Mara", 'Lilith', 'Prim', 'Asher', 'Petra', 'Teacher', 'Mom', 'Kari', 'Iris', 'Mick', 'Roxy', 'Petrov', 'Greta', 'Lilith\'sDad', 'Lilith\'s Aunt']

for direc in direcs:
    files = {}
    print(direc)
    for f in os.listdir("./"+direc):
        doc = docx.Document("./"+direc+"/"+f)
        expressions = {}
        done = False
        missing = set([])
        for line in doc.paragraphs:
            for run in line.runs:
                s = run.text.split()
                if len(s) == 0:
                    continue
                char = s[0].replace('?', '').replace(':', '')
                if char in characters:
                    if len(s)>=3 and '(' in s[1] and ')' in s[2]:
                        if char in missing:
                            missing.remove(char)
                    else:
                        missing.add(char)
        if len(missing) > 0:
            files[f] = missing

    for f in l_sorted(files.keys()):
        print(f'   {f}: ', end='')
        for m in files[f]:
            print(m+' ',end='')
        print()
    
    print()
