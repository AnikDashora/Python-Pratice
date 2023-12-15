def lucas_series(n=10):
    l=[2,1]
    for i in range(n+1):
        l.append(l[i]+l[i+1])
    print(l)
lucas_series(10)