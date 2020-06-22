path = './popular-names.txt'
save_path1 = './col1.txt'
save_path2 = './col2.txt'

with open(path, mode='r') as data_file, \
        open('col1.txt', mode='w') as col1_file, \
        open('col2.txt', mode='w') as col2_file:
    for line in data_file:
        cols = line.split()
        col1_file.write(cols[0] + "\n")
        col2_file.write(cols[1] + "\n")
