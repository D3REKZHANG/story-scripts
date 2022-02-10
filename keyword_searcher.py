import os;
import docx; 

s = [];

direcs = ["Act 1", "Act 2 Prim", "Act 2 Lilith"]
searches = []
n = int(input("# of keywords: "))
for i in range(n):
    searches.append(input("Keyword: ").strip())

total = 0;

for direc in direcs:
    print(direc)
    for f in os.listdir("./"+direc):
        doc = docx.Document("./"+direc+"/"+f)
        found=False
        for line in doc.paragraphs:
            for run in line.runs:
                for search in searches:
                    if search.lower() in run.text.lower():
                        print("    "+f)
                        found=True
                        break
                if found:
                    break
            if found:
                break

