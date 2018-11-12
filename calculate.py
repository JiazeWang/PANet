import fileinput

def calculate():
    a = 0
    for line in fileinput.input("score.txt"):
        a = a + float(line)
    a = float(a/600)
    print(a)

calculate()
