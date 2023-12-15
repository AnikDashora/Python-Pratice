n=5
# for i in range(0,n):
#     for j in  range(i+1):
#         print(" "*(n-i)+"*"*i,end="")
#     print()   

# for i in range(n+1):
#     print(" "*(n-i),"* "*i,end="")
#     print()



# for i in range(3):
#     for j in range(i):
#         if i+j == 2*i :
#             continue
#         else:
#             print(j*"*",end="")
#     print()



# for i in range(5):
#     for j in range(i+1):
#         print((5-i)*" "+i*"*",end = "")
#     print()


# for i in range(5):
#     for j in range(n+1,i+1,-1):
#         print("#",end = " ")
#     print()
n=int(input("Enter: "))

for i in range(n):
    for j in range(i,n-1):
        print(" ",end=" ")
    
    for j in range(i+1):
        print("*",end = " ")
    print()

