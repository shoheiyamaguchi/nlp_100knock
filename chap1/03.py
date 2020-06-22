def main():
    s = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
    l = list((map(lambda x: len(x), s.split())))
    print(l)

main()  