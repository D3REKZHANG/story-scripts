import os, docx;

s = ['Scene 4A.docx',
        'Scene 5A.docx',
        'Scene 7A.docx',
        'Scene 10C.docx',
        'Scene 10D.docx',
        'Scene 11C.docx',
        'Scene 14A.docx',
        'Scene 14B.docx',
        'Scene 14C.docx',
        'Scene 15A.docx',
        'Scene 23.5D.docx',
        'Scene 23A.docx',
        'Scene 24A.docx',
        'Scene 24C.docx',
        'Scene 28A.docx',
        'Scene 29A.docx',
        'Scene 30A.docx',
        'Scene 30B.docx',
        'Scene 31A.docx',
        'Scene 32A.docx',
        'Scene 33A.docx',
        'Scene 34B.docx',
        'Scene 34C.docx',
        'Scene 34E.docx',
        'Scene 34F.docx',
        'Scene 34H.docx',
        'Scene 34I.docx',
        'Scene 34L.docx']

for f in os.listdir("./a"):
    doc = docx.Document("./a/"+f)
    for line in doc.paragraphs:
        if "Prim" in line.text:
            if f not in s:
                print(f)

