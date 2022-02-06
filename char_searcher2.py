import os;
import docx; 

s = [];

chars = ['Mara', 'Lilith', 'Prim', 'Petra', 'Mom', 'Asher', 'Teacher', 'Mitch', 'Iris', 'Kara', 'Petrov', 'Greta' ]
direcs = ['Act 3 Prim']#['Act 1', 'Act 2 Lilith', 'Act 2 Prim', 'Act 3 Lilith','Act 3 Prim']

for char in chars:
    print(char)
    for direc in direcs:
        print(direc)
        for f in os.listdir("./"+direc):
            doc = docx.Document("./"+direc+"/"+f)
            done = False
            for line in doc.paragraphs:
                for run in line.runs:
                    text = run.text.lower().split()
                    if char.lower() in text or char.lower()+'.' in text or char.lower()+":" in text or "?"+char.lower() in text:
                        print("    "+f)
                        done = True
                        break
                if done:
                    break
    print("---------\n")
