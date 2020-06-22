def ngram(s, n):
    s_ngram = set()
    for i in range(0, len(s)-n+1):
        s_ngram.add(s[i:i+n])
    return s_ngram

def main():
    n1 = ngram(s='paraparaparadiser', n=2)
    n2 = ngram(s='paragraph', n=2)
    print(n1 | n2)
    print(n1 & n2)
    print(n1 - n2)
    print('se' in n1)
    print('se' in n2)

main()