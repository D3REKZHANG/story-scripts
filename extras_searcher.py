import docx, os

direcs = ['Act 2 Prim']#['Act 1', 'Act 2 Lilith', 'Act 2 Prim', 'Act 3 Lilith','Act 3 Prim']

chars = ['Pro', 'Mara', 'Lilith', 'Prim', 'Petra', 'Mom', 'Asher', 'Teacher', 'Mitch', 'Iris', 'Kari', 'Petrov', 'Greta', 'Mick']

store = {}

for direc in direcs:
    print(direc)
    for f in os.listdir("./"+direc):
        doc = docx.Document("./"+direc+"/"+f)
        expressions = {}
        done = False
        for line in doc.paragraphs:
            run = line
            s = run.text.split()
            if len(s)>=3 and ':' in run.text and s[0].replace('?','').replace(':','') not in chars:
                char = run.text.split(":")[0]
                if char == 'eyes_closed)':
                    print(run.text)

                if char.isnumeric():
                    continue
                if char in store:
                    store[char].add(f)
                else:
                    store[char] = set([f])

for char in store:
    print(char)
    for f in store[char]:
        print("     "+f)
    print()
