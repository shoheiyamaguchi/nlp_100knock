file_path = 'popular-names.txt'
save_path = 'col'
with open(file_path, 'r') as data_file:
    set_col1 = set()
    for line in data_file:
        cols = line.split()
        set_col1.add(cols[0])

for line in set_col1:
    print(line)
