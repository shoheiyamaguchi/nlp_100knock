import math

n = int(input("--> "))
file_path = 'popular-names.txt'
with open(file_path, mode='r') as data_file:
    lst = data_file.readlines()

    length = len(lst)
    unit = math.ceil(length / n)

    for i, offset in enumerate(range(0, length, unit), 1):
        save_path = 'child_{:02d}.txt'.format(i)
        with open(save_path, mode='w') as out_file:
            for line in lst[offset:offset+unit]:
                out_file.write(line)
