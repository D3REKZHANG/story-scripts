import os, docx, openpyxl
from helper import l_sorted

'''
OPENPYXL SECTION
'''

workbook = openpyxl.load_workbook("character_expressions.xlsx")

sheet = workbook.active

expressions = {}

for col in sheet.iter_cols():
    char = col[0].value
    expressions[char] = []
    for cell in col[1:]:
        if cell.value is None:
            break
        expressions[char].append(cell.value)
        if len(cell.value.split()) != 2:
            print(char + " " + cell.value)

workbook.close()

chars = expressions.keys()

direcs = ['Act 3 Prim']

errors = {}

unlisted = set()
 
for direc in direcs:
    for f in os.listdir("./"+direc):
        doc = docx.Document("./"+direc+"/"+f)
        for line in doc.paragraphs:
            for run in line.runs:
                s = run.text.split()
                if len(s)>=3:
                    x = 0
                    if s[0] == 'Lilith’s':
                        if len(s) < 4:
                            continue
                        x = 1
                        if s[1] == 'Aunt':
                            char = 'Lilith\'s Aunt'
                        else:
                            char = 'Lilith\'s Dad'
                    else:
                        char = s[0].replace('?', '').replace(':','')

                    if '(' in s[x+1] and ')' in s[x+2]:
                        if char not in chars:
                            unlisted.add(f"{direc}/{f}: {char}")
                            continue
                        b1 = s[x+1].index('(')
                        b2 = s[x+2].index(')')
                        expr = s[x+1][b1+1:] + " " + s[x+2][:b2]
                        if expr not in expressions[char]:
                            file = f"{direc}/{f}"
                            expr = f"{char} ({expr})"
                            if expr in errors:
                                if file not in errors[expr]:
                                    errors[expr].add(f"{direc}/{f}")
                            else:
                                errors[expr] = set([file])

for key in sorted(errors.keys()):
    print(key)
    for f in l_sorted(errors[key]):
        print("    " + f)
    print()

print("UNLISTED --------- ")
for error in unlisted:
    print(error)
