#code
for _ in range(int(input())):
    l=int(input())
    a=list(map(int, input().split()))
    a = a[::-1]
    for i in range(l):
        print(a[i], end=" ")
    print()