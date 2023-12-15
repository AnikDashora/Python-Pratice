def fibonacci_series(n):
    l=[0,1]
    for i in range(n+1):
        l.append(l[i]+l[i+1])
    print(l)
    # print(sum(l))

# fibonacci_series(10)
n=int(input("vamuw of n? "))
l1=[0,1]
i=0
while i <= n-2:
    l1.append(l1[i]+l1[i+1])
    i+=1

print(l1,sum(l1))
