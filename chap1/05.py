def main(s, n):
    l = s.split()
    for i in range(0, len(l)-n+1):
        print(" ".join(l[i:i+n]))

main(s='I am an NLPer', n=2)  