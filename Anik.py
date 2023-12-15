# n=int(input("pick:"))
# x=1
# i=1
# while i<=n: 
#     x=i*x
#     i=i+1

  
# print(x)

# print("-----------------------------------")


# t=1
# y=0
# while t<=n:
#     t=t+1

#     if t%2==0:

#         y=y+t

# print(y)


# print("-----------------------------------")

# q=1
# i=1
# while i<=n:
#     q=i*q
#     i=i+2
       
# print(q)        
# print("-----------------------------------")
# w=1
# i=0
# while i<=n:
#     if i%2 != 0:
#         w=w*i
#     i=i+1    

# print(w)        

# print("-----------------------------------")
# # if range(0,n,jump value) then its 0 to n-1, jump value is set to equal to 1
# i=1
# for i in range(1,21,2):
#     print(i,end= " , ")
#     print(type(i))
# t=n

# s=0
# for i in range(1,n):
#     if n % i == 0:
#         s+=i

# if s==t:
#     print("it is a perfect number")
# else:
#     print("it is not perfect number")    


import random 
print(random.random())   # float value of 0.02 to 1.25
print(random.uniform(2,5)) # float b/w a,b
print(random.randint(1,5))   # int
print(random.getrandbits(1)) 
a=[1,2,3,4,5,6,7,90]        
print(random.choice(a[0:5]))
