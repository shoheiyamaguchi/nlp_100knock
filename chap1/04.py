def main():
    s = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
    l = list(s.split())
    ans = {str(i+1): l[i][0] if i+1 in [1, 5, 6, 7, 8, 9, 15, 16, 19] else l[i][:2] for i in range(0, 19)}
    print(ans)

main()  