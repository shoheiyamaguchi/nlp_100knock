n = int(input('N--> '))
with open('popular-names.txt', mode='r') as f:
    for i, line in enumerate(f):
        if i >= n:
            break
        print(line.rstrip())
