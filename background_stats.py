import docx, os, sys

print("Background Stats")
print("(1) Locations")
print("(2) Occurences")
mode = int(input("> "))
print()

backgrounds = {}
with open('backgrounds.txt', 'r') as f:
    for line in f:
        if mode == 1:
            backgrounds[line.strip()] = set()
        else:
            backgrounds[line.strip()] = 0

non_bg = {}

if mode == 1:
    cutscenes = {}
else:
    cutscenes = set()

direcs = ["Act 1", "Act 2 Lilith", "Act 2 Prim"]#, "Act 3 Prim", "Act 3 Lilith"]

for direc in direcs:
    for f in os.listdir(f'./{direc}'):
        doc = docx.Document("./"+direc+"/"+f)
        for line in doc.paragraphs:
            if line.runs[0].bold:
                if 'OR' in line.text:
                    continue
                cleaned = line.text.replace("’", "'").replace("–", "-")

                if 'Cutscene' in cleaned or 'Nostalgia' in cleaned or 'End Scene' in cleaned:
                    if mode == 1:
                        if cleaned in cutscenes:
                            cutscenes[cleaned].add(f'{direc}/{f}')
                        else:
                            cutscenes[cleaned] = set([f'{direc}/{f}'])
                    else:
                        cutscenes.add(cleaned)
                    continue

                if cleaned in backgrounds:
                    if mode == 1:
                        backgrounds[cleaned].add(f'{direc}/{f}')
                    else:
                        backgrounds[cleaned]+=1
                elif cleaned in non_bg:
                    non_bg[cleaned].add(f'{direc}/{f}')
                else:
                    non_bg[cleaned] = set([f'{direc}/{f}'])

if mode == 1:
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
else:
    for bg in sorted(backgrounds.keys(), key=lambda x: -backgrounds[x]):
        print(f'{bg:<30} {backgrounds[bg]}')

    
print("\nCUTSCENES ----------\n")

for bg in cutscenes:
    print(bg)
    if mode == 1:
        for f in cutscenes[bg]:
            print("    "+f)
        print()

print("\nERRORS ----------\n")

for bg in non_bg:
    print(bg)
    for f in non_bg[bg]:
        print("    "+f)
    print()

