path = './popular-names.txt'

with open(path) as f:
    s = f.readlines()
    print(len(s))