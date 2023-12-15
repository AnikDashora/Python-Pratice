def ncr(n,r):
    a=1
    b=1
    c,d=n-r,1
    for z in range(1,n+1):
        a=a*z
    # print(a)        
    for x in range(1,r+1):
        b=b*x
    # print(b)    
    for y in range(1,c+1):
        d=d*y
    return int(a/(b*d))

q=int(input("Enter number: "))

for i in range(q):
    for j in range(i+1):
        
        print(ncr(i,j),end=" ")
    print()   

    
# for i in range(q):
#     for j in range(i+1):
#         print(f"{i}C{j} ",end=" ")
#     print()  
# 
# 
     