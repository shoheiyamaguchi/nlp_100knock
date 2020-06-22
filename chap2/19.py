import collections

file_path = 'popular-names.txt'
lines = open(file_path).readlines()
lst = [line.split()[0] for line in lines]

count = collections.Counter(lst)
count_l = count.items()
count_l = sorted(count_l, key=lambda x: int(x[1]), reverse=True)
for k, v in count_l:
    print(k, v)
