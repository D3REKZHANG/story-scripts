import os;
import docx; 
from helper import l_sorted

s = [];

direcs = ["Act 1", "Act 2 Prim", "Act 2 Lilith", "Act 3 Lilith", "Act 3 Prim"]
searches = []
o = input('case sensitive? (y/n) ')

sens = True if o.strip() == 'y' else False

n = int(input("# of keywords: "))
for i in range(n):
    searches.append(input("Keyword: ").strip())

total = 0;

l = {}

for direc in direcs:
    l[direc] = []
    for f in os.listdir("./"+direc):
        doc = docx.Document("./"+direc+"/"+f)
        found=False
        for line in doc.paragraphs:
            for run in line.runs:
                for search in searches:
                    if (not sens and search.lower() in run.text.lower()) or (sens and search in run.text):
                        l[direc].append(f)
                        found=True
                        break
                if found:
                    break
            if found:
                break

for d in l:
    print(d)
    for f in l_sorted(l[d]):
        print("    "+f)
    print()
