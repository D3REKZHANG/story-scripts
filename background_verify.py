import docx, os, sys

backgrounds = {}
with open('backgrounds.txt', 'r') as f:
    for line in f:
        backgrounds[line.strip()] = set()

non_bg = {}

cutscenes = {}

direcs = ["Act 1", "Act 2 Lilith", "Act 2 Prim"]#, "Act 3 Prim", "Act 3 Lilith"]

for direc in direcs:
    for f in os.listdir(f'./{direc}'):
        doc = docx.Document("./"+direc+"/"+f)
        for line in doc.paragraphs:
            for run in line.runs:
                if run.bold:
                    if 'OR' in run.text:
                        continue
                    cleaned = run.text.replace("’", "'").replace("–", "-")

                    if 'Cutscene' in cleaned or 'Nostalgia' in cleaned:
                        if cleaned in cutscenes:
                            cutscenes[cleaned].add(f'{direc}/{f}')
                        else:
                            cutscenes[cleaned] = set([f'{direc}/{f}'])
                        continue

                    if cleaned in backgrounds:
                        backgrounds[cleaned].add(f'{direc}/{f}')
                    elif cleaned in non_bg:
                        non_bg[cleaned].add(f'{direc}/{f}')
                    else:
                        non_bg[cleaned] = set([f'{direc}/{f}'])

empty = []
for bg in backgrounds:
    if len(backgrounds[bg]) == 0:
        empty.append(bg)
        continue
    print(bg)
    for f in sorted(backgrounds[bg]):
        print("    "+f)
    print()

print("Backgrounds not used:")
for e in empty:
    print(e)
    
print("\nCUTSCENES ----------\n")

for bg in cutscenes:
    print(bg)
    for f in cutscenes[bg]:
        print("    "+f)
    print()

print("\nOTHER ----------\n")

for bg in non_bg:
    print(bg)
    for f in non_bg[bg]:
        print("    "+f)
    print()

