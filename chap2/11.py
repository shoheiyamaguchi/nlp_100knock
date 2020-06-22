path = './popular-names.txt'

with open(path) as f:
    #for line in f:
    s = f.read()
    s = s.replace('\t', ' ')
    print(s)
