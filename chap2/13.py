with open('col1.txt', mode='r') as col1, \
        open('col2.txt', mode='r') as col2, \
        open('merge.txt', mode='w') as merge:
    for col1_line, col2_line in zip(col1, col2):
        merge_line = col1_line.strip() + "\t" + col2_line.strip() + "\n"
        merge.write(merge_line)
