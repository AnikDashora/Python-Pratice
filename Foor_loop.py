# n= int(input("pick"))
# x=0

# while n >= 1:
#     rem = n%10
#     x = x+rem
#     n = n//10
# print(x)




n=int(input("pick"))
q=n

y=len(str(n))
x=0

# while n >= 1:
#     rem = n%10
#     x = x+(rem**y)
#     n = n//10


# if x==q:
#     print("it is")
# else:
#     print("no")   


# e=str(n)
# f=e[::-1]
# z=int(f)
# print(z) 
i=0

while i<=y:
    rem = n%10
    x = x+(rem*(y-i))
    n = n//10
    i=i+1

print(x)    



        












    

