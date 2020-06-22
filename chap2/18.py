file_path = 'popular-names.txt'
with open(file_path) as data_file:
    lst = []
    for line in data_file:
        cols = line.split()
        lst.append(cols)
    lst.sort(key=lambda x: int(x[2]), reverse=True)
    for line in lst:
        line = "\t".join(line)
        
