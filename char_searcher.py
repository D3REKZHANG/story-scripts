import os;
import docx; 

s = [];

direcs = ['Act 3 Prim']#['Act 1', 'Act 2 Lilith', 'Act 2 Prim', 'Act 3 Lilith','Act 3 Prim']

n= int(input("# of char: "))

strict = False
if n > 1:
    inp = input("Strict? (y/n): ")
    if inp.strip() == 'y':
        strict = True

searches = []
for i in range(n):
    searches.append(str(input("Character: ")))

total = 0;

for direc in direcs:
    print(direc)
    for f in os.listdir("./"+direc):
        doc = docx.Document("./"+direc+"/"+f)
        found = []
        done = False
        for line in doc.paragraphs:
            for run in line.runs:
                for search in searches:
                    if search in found:
                        continue
                    text = run.text.lower().split()
                    if search.lower() in text or search.lower()+'.' in text or search.lower()+":" in text or "?"+search.lower() in text:
                        found.append(search)
                        if not strict:
                            print("    "+f)
                            done = True
                            break
                    if len(found) == len(searches):
                        print("    "+f)
                        break
                if done:
                    break
            if done or len(found) == len(searches):
                break

for f in s:
    print(f)
