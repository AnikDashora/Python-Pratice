# n=input("enter: ")
# z = n.strip("")
# s = 0
# for i in z:
#     s= s+int(i)**len(z)

# if int(n) == s:
#     print("It is")
# else:
#     print("It is not")

n=int(input("Enter: "))
z=str(n)
# q = z.split()
# print(q)
s = 0
for i in z:
    s = s +int(i)**len(z)

if n == s:
    print("It is")
else:
    print("It is not")