n=8

def fnc_s(n):
    if n<=2:
        return 1
    else:
        return fnc_s(n-2) + fnc_s(n-1)

for i in range(1, n+1):
    print(fnc_s(i))
