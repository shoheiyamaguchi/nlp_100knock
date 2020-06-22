n = int(input("n--> "))
file_path = 'popular-names.txt'
with open(file_path, mode='r') as f:
    lst = f.readlines()
    for line in lst[-n:]:
        print(line.rstrip())
