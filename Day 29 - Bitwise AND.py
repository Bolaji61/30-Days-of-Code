t = int(input())

for t_itr in range(t):
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])

    list_ab = [(i,j) for i in range(1, n+1) for j in range(i+1, n+1)]

    ab = [i & j for (i,j) in list_ab if k>i & j]

    print(max(ab))
