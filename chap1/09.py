import random

def main(s='I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'):
    l = s.split()
    for i in range(len(l)):
        if len(l[i]) >= 5:
            l[i] = "".join([l[i][0]] + random.sample(l[i][1:-1], len(l[i][1:-1])) + [l[i][-1]])
    print(' '.join(l))

main()
    