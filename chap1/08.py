def main(s='agaargraratahaAFEFJOjfaiga'):
    l = list(s)
    for i in range(len(l)):
        if l[i].islower():
            l[i] = chr(219 - ord(l[i]))
    print("".join(l))

main()
