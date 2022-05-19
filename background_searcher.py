import os;
import docx; 

direc = str(input("Directory: "))

backgrounds = {}

total = 0;

for f in os.listdir("./"+direc):
    doc = docx.Document("./"+direc+"/"+f)
    print(f"-------{f}-------")
    for line in doc.paragraphs:
        for run in line.runs:
            if run.bold and 'OR' not in run.text and run.text.split()[0] != 'Nostalgia':
                print("    "+run.text)
                '''
                if run.text in backgrounds:
                    backgrounds[run.text] += 1
                else:
                    backgrounds[run.text] = 1
                '''

backgrounds = dict(sorted(backgrounds.items(), key=lambda item: item[1],reverse=True))

for key in backgrounds:
    print(f"{key}: {backgrounds[key]}")





