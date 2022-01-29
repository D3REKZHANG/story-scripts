import os, docx, openpyxl; 
from openpyxl.styles import *;

direc = str(input("Directory: "))

store = {}

for f in os.listdir("./"+direc):
    doc = docx.Document("./"+direc+"/"+f)
    print(f)
    for line in doc.paragraphs:
        for run in line.runs:
            s = run.text.split()
            if len(s)>=3:
                if '(' in s[1] and ')' in s[2]:
                    b1 = s[1].index('(')
                    b2 = s[2].index(')')
                    char = s[0]
                    if "?" in char:
                        if(char[0] != '?'):
                            print(f"Unexpected Behaviour in {doc}: \"{char}\"")
                        char = char[1:]
                    if ":" in char:
                        char = char.replace(":", "")
                    pose = s[1][b1+1:]
                    expr = s[2][:b2]
                    if char in store:
                        if pose in store[char]:
                            store[char][pose].add(expr)
                        else:
                            store[char][pose] = set([expr])
                    else:
                        store[char] = { pose : set([expr]) }

print(store.keys())

'''
OPENPYXL SECTION
'''

workbook = openpyxl.Workbook()

workbook.remove(workbook['Sheet'])

for char in store:
    sheet = workbook.create_sheet(title=char)
    sheet["A1"] = "POSES"
    sheet["A1"].fill = PatternFill(patternType='solid', fill_type='solid', fgColor=Color('96BAE6'))
    sheet["A2"] = "EXPRESSIONS"

    sheet.column_dimensions["A"].width = len("Expression")+4
    sheet.freeze_panes = sheet["B2"]
    cur = "B"

    for pose in store[char]:
        sheet[cur+"1"] = pose
        sheet[cur+"1"].fill = PatternFill(patternType='solid', fill_type='solid', fgColor=Color('C5D9F1'))
        maxLen = 0
        for expr, i in zip(store[char][pose], range(1, 1+len(store[char][pose]))):
            sheet[cur+str(i)] = expr
            maxLen = max(maxLen, len(expr))

        # set column width
        sheet.column_dimensions[cur].width = maxLen+2

        if cur[-1] == 'Z':
            cur = "A"*(len(cur)+1)
        else:
            cur = cur[1:]+chr(ord(cur[-1])+1)


workbook.save(filename=direc+" expressions.xlsx")
