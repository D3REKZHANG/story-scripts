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
            if line.runs[0].bold:
                if 'OR' in line.text:
                    continue
                cleaned = line.text.replace("’", "'").replace("–", "-")

                if 'Cutscene' in cleaned or 'Nostalgia' in cleaned or 'End Scene' in cleaned:
                    continue

                if cleaned not in backgrounds:
                    if cleaned in non_bg:
                        non_bg[cleaned].add(f'{direc}/{f}')
                    else:
                        non_bg[cleaned] = set([f'{direc}/{f}'])

print("\nERRORS? ----------\n")

for bg in non_bg:
    print(bg)
    for f in non_bg[bg]:
        print("    "+f)
    print()

