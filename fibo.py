n=8

def f(n):
    if n<=2:
        return 1
    else:
        return f(n-2) + f(n-1)

for i in range(1, n+1):
    print(f(i))
